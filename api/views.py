from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from api.models import ZwardyFarmers, OdkclientFarmeridhistory as FarmerHistory
from api.serializers import ZwardyFarmersSerializer

class ZwardyFarmerView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    def get_from_farmer_table(self, farmer_id):
        try:
            return ZwardyFarmers.objects.get(farmer_id=farmer_id)
        except ZwardyFarmers.DoesNotExist:
            return None
        
    def get_from_farmer_history(self, farmer_id):
        try:
            return FarmerHistory.objects.get(new_farmer_id=farmer_id)
        except FarmerHistory.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, farmer_id, *args, **kwargs):
        farmer = self.get_from_farmer_table(farmer_id)
        farmer_history = self.get_from_farmer_history(farmer_id=farmer_id)

        id_type = request.GET.get("id_type")
        print(id_type)

        if not farmer and not farmer_history:
            return Response(
                {
                    "message": f"Farmer {farmer_id} does not exist"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        
        if not farmer:
            farmer = self.get_from_farmer_table(farmer_history.old_farmer_id)

        if not farmer:
            return Response(
                {
                    "message": f"Farmer {farmer_id} exists on farmer_history table but is missing from farmer table"
                },
                status=status.HTTP_503_SERVICE_UNAVAILABLE
            )

        farmer_serializer = ZwardyFarmersSerializer(farmer)
        res_json = farmer_serializer.data

        # All IDs
        all_ids = []
        all_ids.append(farmer.farmer_id)

        if farmer_history:
            for farmer_from_h in farmer_history:
                if farmer_from_h.old_farmer_id not in all_ids:
                    all_ids.append(farmer_history.old_farmer_id)
                if not farmer_from_h.new_farmer_id in all_ids:
                    all_ids.append(farmer_history.new_farmer_id)

        res_json['farmer_id_data'] = {
            'current': farmer_id,
            'original': farmer.farmer_id,
            'all': all_ids
        }
        return Response(res_json, status=status.HTTP_200_OK)

