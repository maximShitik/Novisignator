from flask import Blueprint

admin_bp = Blueprint('admin', __name__)

# Stores
@admin_bp.route('/admin/stores', methods=['GET'])
def get_stores():
    pass

@admin_bp.route('/admin/stores', methods=['POST'])
def create_store():
    pass

@admin_bp.route('/admin/stores/<int:id>', methods=['PUT'])
def update_store(id):
    pass

@admin_bp.route('/admin/stores/<int:id>', methods=['DELETE'])
def delete_store(id):
    pass

# Products
@admin_bp.route('/admin/products', methods=['GET'])
def get_products():
    pass

@admin_bp.route('/admin/products', methods=['POST'])
def create_product():
    pass

@admin_bp.route('/admin/products/<int:id>', methods=['PUT'])
def update_product(id):
    pass

@admin_bp.route('/admin/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    pass

# Coupons
@admin_bp.route('/admin/coupons', methods=['GET'])
def get_coupons():
    pass

@admin_bp.route('/admin/coupons', methods=['POST'])
def create_coupon():
    pass

@admin_bp.route('/admin/coupons/<int:id>', methods=['PUT'])
def update_coupon(id):
    pass

@admin_bp.route('/admin/coupons/<int:id>', methods=['DELETE'])
def delete_coupon(id):
    pass

# Ads
@admin_bp.route('/admin/ads', methods=['GET'])
def get_ads():
    pass

@admin_bp.route('/admin/ads', methods=['POST'])
def create_ad():
    pass

@admin_bp.route('/admin/ads/<int:id>', methods=['PUT'])
def update_ad(id):
    pass

@admin_bp.route('/admin/ads/<int:id>', methods=['DELETE'])
def delete_ad(id):
    pass

# Scan Points
@admin_bp.route('/admin/scan-points', methods=['GET'])
def get_scan_points():
    pass

@admin_bp.route('/admin/scan-points', methods=['POST'])
def create_scan_point():
    pass

@admin_bp.route('/admin/scan-points/<int:id>', methods=['PUT'])
def update_scan_point(id):
    pass

@admin_bp.route('/admin/scan-points/<int:id>', methods=['DELETE'])
def delete_scan_point(id):
    pass

# Navigation Routes
@admin_bp.route('/admin/routes', methods=['GET'])
def get_routes():
    pass

@admin_bp.route('/admin/routes', methods=['POST'])
def create_route():
    pass

@admin_bp.route('/admin/routes/<int:id>', methods=['PUT'])
def update_route(id):
    pass

@admin_bp.route('/admin/routes/<int:id>', methods=['DELETE'])
def delete_route(id):
    pass