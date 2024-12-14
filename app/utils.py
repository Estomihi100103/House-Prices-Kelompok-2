def validate_input(data):
    """Fungsi validasi input umum"""
    if not data:
        return False
    return True

def format_response(status, message, data=None):
    """Fungsi untuk memformat respons API"""
    response = {
        'status': status,
        'message': message
    }
    if data:
        response['data'] = data
    return response