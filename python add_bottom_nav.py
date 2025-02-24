import os
from bs4 import BeautifulSoup

# HTML cho bottom navigation
BOTTOM_NAV_HTML = """
<!-- Bottom Navigation Bar -->
<div class="bottom-nav">
    <div class="container">
        <div class="row">
            <div class="col-12">
                <div class="bottom-nav-menu" style="display: flex; justify-content: space-around; align-items: center;">
                    <a href="/">
                        <i class="fas fa-home"></i>
                        <span>Home</span>
                    </a>
                    <a href="/category/new.html">
                        <i class="fas fa-star"></i>
                        <span>New</span>
                    </a>
                    <a href="/category/popular.html">
                        <i class="fas fa-fire"></i>
                        <span>Popular</span>
                    </a>
                    <a href="/category/categories.html">
                        <i class="fas fa-th-large"></i>
                        <span>Categories</span>
                    </a>
                </div>
            </div>
        </div>
    </div>
</div>
"""

def add_bottom_nav(html_file):
    try:
        with open(html_file, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'html.parser')
            
        # Kiểm tra xem bottom-nav đã tồn tại chưa
        if not soup.select_one('.bottom-nav'):
            # Tìm thẻ body
            body = soup.find('body')
            if body:
                # Thêm bottom nav trước thẻ đóng body
                bottom_nav_soup = BeautifulSoup(BOTTOM_NAV_HTML, 'html.parser')
                body.append(bottom_nav_soup)
                
                # Lưu file
                with open(html_file, 'w', encoding='utf-8') as file:
                    file.write(str(soup))
                print(f"Đã thêm bottom nav vào {html_file}")
            else:
                print(f"Không tìm thấy thẻ body trong {html_file}")
    except Exception as e:
        print(f"Lỗi khi xử lý {html_file}: {str(e)}")

def process_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                html_file = os.path.join(root, file)
                add_bottom_nav(html_file)

# Thư mục gốc của website
root_directory = '.'  # Thay đổi đường dẫn này theo thư mục của bạn

# Các thư mục cần xử lý
directories = [
    './category',
    './go',
    '.'  # thư mục gốc cho các file html ở root
]

# Xử lý từng thư mục
for directory in directories:
    if os.path.exists(directory):
        print(f"\nĐang xử lý thư mục: {directory}")
        process_directory(directory)
    else:
        print(f"Thư mục không tồn tại: {directory}")

print("\nHoàn thành!")