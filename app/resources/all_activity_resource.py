from flask_restful import Resource

from app.resources import KeyPressResource, LeftClickResource, RightClickResource, MouseMovementResource

class AllActivityResource(Resource):
    def get(self):
        try:
            key_presses = KeyPressResource().get_data()
            left_clicks = LeftClickResource().get_data()
            right_clicks = RightClickResource().get_data()
            mouse_movements = MouseMovementResource().get_data()

            # Aggregate all data
            all_data = {
                'keyPresses': key_presses,
                'leftClicks': left_clicks,
                'rightClicks': right_clicks,
                'mouseMovements': mouse_movements
            }

            return {'data': all_data}, 200
        except Exception as e:
            return {"message": f"Error retrieving data: {str(e)}"}, 500