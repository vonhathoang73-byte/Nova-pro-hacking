#  _   _                 _
# | \ | |               (_)
# |  \| | __ ___   __ _  _
# | . ` |/ _` \ \ / /(_)| |
# | |\  | (_| |\ V /  _ | |
# |_| \_|\__,_| \_/  (_)|_|
#
# Navi Đa Công Cụ - Phát triển bởi vonhathoang
# GitHub: https://github.com/glockinhand/navi-multitool

import os
import sys
import shutil
import re
import random
try:
    import psutil
except ImportError:
    psutil = None

from core.display import Theme, Colorate, Colors, clr, get_config

PAGES = [
    {
        "title": "CÔNG CỤ DISCORD",
        "description": "Thao tác API, tiện ích token, quản lý máy chủ",
        "tools": [
            ("1", "Nova_Pro", "Spam hoặc xóa webhook Discord"),
            ("2", "Công cụ Token", "Thông tin, nuke tài khoản, đăng nhập & xoay vòng token"),
            ("3", "Trình tạo Nitro", "Tạo mã quà tặng Nitro đa luồng"),
            ("4", "Thông tin Máy chủ", "Lấy chi tiết máy chủ từ link mời"),
            ("5", "Tạo link mời Bot", "Tạo link mời bot có quyền admin"),
            ("6", "Selfbot", "Khởi chạy menu selfbot tùy chỉnh"),
            ("7", "Sao chép Máy chủ", "Sao chép máy chủ Discord bằng token"),
            ("8", "Bot Nuke", "Bảng điều khiển bot phá hủy máy chủ nâng cao"),
            ("9", "Kiểm tra Tên", "Kiểm tra tính khả dụng của tên người dùng Discord")
        ]
    },
    {
        "title": "OSINT & MẠNG",
        "description": "IP, DNS, whois, định vị số điện thoại và theo dõi dox",
        "tools": [
            ("10", "Quét Cổng", "Quét các cổng mở trên máy chủ đích"),
            ("11", "Tra cứu Whois", "Lấy thông tin đăng ký tên miền"),
            ("12", "Tra cứu DNS", "Tra cứu bản ghi DNS (A, MX, TXT...)"),
            ("14", "Theo dõi Dox", "Tra cứu cơ sở dữ liệu thông tin dox"),
            ("15", "Tạo Dox", "Tạo hồ sơ dox tùy chỉnh"),
            ("16", "Tra cứu SĐT", "Tra cứu nhà mạng và vị trí số điện thoại"),
            ("17", "Tra cứu Email", "Lấy dữ liệu OSINT liên kết với email")
        ]
    },
    {
        "title": "CÔNG CỤ ĐỘC HẠI",
        "description": "DDoS, lỗ hổng, quét ví và xây payload",
        "tools": [
            ("20", "Bom Email", "Gửi email spam đến địa chỉ mục tiêu"),
            ("21", "Clipper Tiền ảo", "Xây dựng clipper chiếm quyền clipboard"),
            ("22", "Quét Lỗ hổng", "Quét các lỗ hổng phổ biến trên mục tiêu"),
            ("23", "Tấn công DDoS", "Thực hiện kiểm tra tải mạng lưu lượng cao"),
            ("24", "Xây Stealer", "Biên dịch payload đánh cắp mật khẩu và token"),
            ("25", "Xây Keylogger", "Xây dựng ứng dụng ghi phím ẩn"),
            ("26", "Lấy IP", "Tạo link theo dõi ghi lại IP khách truy cập"),
            ("27", "Xây RAT", "Xây dựng bản cài Trojan truy cập từ xa"),
            ("28", "Bruteforce Ví", "Bruteforce cụm từ khôi phục ví tiền ảo")
        ]
    },
    {
        "title": "TIỆN ÍCH ROBLOX",
        "description": "Công cụ cookie, đăng nhập tài khoản, quản lý nhóm",
        "tools": [
            ("40", "Thông tin Người dùng", "Lấy chi tiết tài khoản Roblox"),
            ("41", "Thông tin Cookie", "Xác thực và kiểm tra cookie Roblox"),
            ("42", "Đăng nhập Cookie", "Đăng nhập Roblox trực tiếp bằng cookie"),
            ("43", "Thông tin Nhóm", "Phân tích chi tiết nhóm Roblox mục tiêu"),
            ("44", "Tải Asset", "Tải xuống asset game, texture áo/quần"),
            ("45", "Lịch sử Tên", "Theo dõi và hiển thị tên cũ của tài khoản"),
            ("46", "Kiểm tra Tên", "Kiểm tra tính khả dụng tên Roblox"),
            ("47", "Làm mới Cookie", "Tạo cookie mới từ cookie hiện có")
        ]
    },
    {
        "title": "GIẢ LẬP & MÔ PHỎNG",
        "description": "Công cụ phishing, sao chép web, mô phỏng giao diện",
        "tools": [
            ("50", "Công cụ Giả", "Truy cập 17 mô phỏng như Fake Nitro, Exodus, OTP PayPal"),
            ("34", "Sao chép Web", "Sao chép mã nguồn HTML của trang mục tiêu"),
            ("35", "Tạo QR", "Tạo mã QR tiêu chuẩn và giả mạo")
        ]
    },
    {
        "title": "HỆ THỐNG & TỔNG HỢP",
        "description": "Codec, làm rối, metadata, cài đặt ứng dụng",
        "tools": [
            ("30", "Codec Base64", "Mã hóa hoặc giải mã chuỗi bằng Base64"),
            ("31", "Thông tin Hệ thống", "Xem thông số phần cứng máy tính"),
            ("32", "Ping IP", "Ping IP đích để kiểm tra độ trễ và khả dụng"),
            ("33", "Làm rối Mã", "Làm rối mã Python để chống dịch ngược"),
            ("13", "Quét Metadata", "Phân tích và xóa metadata EXIF khỏi file ảnh"),
            ("60", "Thông tin Ứng dụng", "Hiển thị phiên bản, giấy phép và nhà phát triển"),
            ("61", "Cấu hình Ứng dụng", "Quản lý giao diện, cập nhật, khởi động"),
            ("62", "Vô hiệu hóa Antivirus", "Thêm ổ C vào ngoại lệ Defender để tránh gián đoạn"),
            ("63", "Gỡ rác Windows", "Khởi chạy tiện ích gỡ rác và tối ưu Windows"),
            ("64", "Thu thập Proxy", "Thu thập proxy HTTP, SOCKS4, SOCKS5"),
            ("65", "Kiểm tra Proxy", "Kiểm tra độ trễ và hợp lệ của proxy đã thu thập")
        ]
    }
]

def _strip(_t):
    return re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])').sub('', _t)

class PaginatedUI:
    ACTIVE_LOGO = None
    @staticmethod
    def get_layout_width():
        tw = shutil.get_terminal_size().columns
        return max(74, min(100, tw - 4))
    @staticmethod
    def get_margin(box_w):
        tw = shutil.get_terminal_size().columns
        return " " * max(0, (tw - box_w) // 2)
    @staticmethod
    def draw_tabs(active_idx, colors, box_w, margin):
        inner = box_w - 2
        sep = " │ "
        tab_names = ["DISCORD", "OSINT", "ĐỘC HẠI", "ROBLOX", "GIẢ LẬP", "HỆ THỐNG"]
        short_names = ["DISC", "OSINT", "ĐỘC", "RBLX", "GIẢ", "HỆ"]
        def build_tab_line(names):
            labels = []
            for idx, name in enumerate(names):
                if idx == active_idx:
                    labels.append(f"► {name} ◄")
                else:
                    labels.append(f" {name} ")
            return sep.join(labels)
        tab_line = build_tab_line(tab_names)
        if len(tab_line) > inner:
            tab_line = build_tab_line(short_names)
        if len(tab_line) > inner:
            labels = []
            for idx in range(len(tab_names)):
                if idx == active_idx:
                    labels.append(f"►{idx+1}◄")
                else:
                    labels.append(f"[{idx+1}]")
            tab_line = sep.join(labels)
        pad = max(0, (inner - len(tab_line)) // 2)
        extra = max(0, inner - len(tab_line) - pad * 2)
        pad_str = " " * pad
        extra_str = " " * extra
        top = "╔" + "═" * inner + "╗"
        bot = "╚" + "═" * inner + "╝"
        parts = tab_line.split(sep)
        colored_content = ""
        for idx, part in enumerate(parts):
            if "►" in part:
                colored_content += Colorate.Horizontal(colors["banner"], part)
            else:
                colored_content += Colorate.Horizontal(colors["txt"], part)
            if idx < len(parts) - 1:
                colored_content += Colorate.Horizontal(colors["num"], sep)
        print(margin + Colorate.Horizontal(colors["num"], top))
        print(margin + "║" + pad_str + colored_content + pad_str + extra_str + "║")
        print(margin + Colorate.Horizontal(colors["num"], bot))
    @staticmethod
    def draw_page_content(active_idx, colors, box_w, margin):
        page = PAGES[active_idx]
        inner = box_w - 2
        title = f" {page['title']} - {page['description']} "
        if len(title) > inner:
            title = f" {page['title']} "
        border_len = max(2, (inner - len(title)) // 2)
        extra_dash = "─" if (inner - len(title)) % 2 != 0 else ""
        top = "┌" + "─" * border_len + title + "─" * border_len + extra_dash + "┐"
        print(margin + Colorate.Horizontal(colors["head"], top))
        print(margin + Colorate.Horizontal(colors["num"], "│" + " " * inner + "│"))
        name_col_w = max(15, min(22, inner // 4))
        opt_w = 9
        for num, name, desc in page["tools"]:
            opt = f"  [{num.zfill(2)}] "
            name_pad = " " * max(1, name_col_w - len(name))
            sep_str = "─  "
            max_desc = inner - len(opt) - name_col_w - len(sep_str) - 2
            disp_desc = desc[:max_desc - 3] + "..." if len(desc) > max_desc else desc
            plain = f"{opt}{name}{name_pad}{sep_str}{disp_desc}"
            pad_right = " " * max(0, inner - len(plain))
            line = (
                Colorate.Horizontal(colors["num"], "│") +
                Colorate.Horizontal(colors["num"], opt) +
                Colorate.Horizontal(colors["txt"], name) +
                Colorate.Horizontal(colors["num"], name_pad + sep_str) +
                Colorate.Horizontal(colors["txt"], disp_desc) +
                pad_right +
                Colorate.Horizontal(colors["num"], "│")
            )
            print(margin + line)
        print(margin + Colorate.Horizontal(colors["num"], "│" + " " * inner + "│"))
        print(margin + Colorate.Horizontal(colors["head"], "└" + "─" * inner + "┘"))

    @staticmethod
    def draw_footer(colors, box_w, margin):
        inner = box_w - 2
        nav_str = " [P/N] Trang Trước/Sau  │  [60] Thông tin  │  [61] Cài đặt  │  [99] ~ Nova-Pro "

        if len(nav_str) > inner:
            nav_str = " [P/N] Trang  │  [60] Info  │  [61] Set  │  [99] Thoát "
        pad = max(0, (inner - len(nav_str)) // 2)
        extra = max(0, inner - len(nav_str) - pad * 2)
        mid = "│" + " " * pad + nav_str + " " * pad + " " * extra + "│"
        print(margin + Colorate.Horizontal(colors["num"], "┌" + "─" * inner + "┐"))
        print(margin + Colorate.Horizontal(colors["txt"], mid))
        print(margin + Colorate.Horizontal(colors["num"], "└" + "─" * inner + "┘"))
        cfg = get_config()
        user = os.environ.get('USERNAME') or os.environ.get('USER') or 'Người dùng'
        ver = cfg.get("version", "2.0.0")
        stats_str = ""
        if psutil:
            try:
                cpu = int(psutil.cpu_percent())
                ram = int(psutil.virtual_memory().percent)
                stats_str = f" │ cpu: {cpu}% │ ram: {ram}%"
            except:
                pass

        small_info = f"v{ver}{stats_str}"
        tw = shutil.get_terminal_size().columns
        print(Colorate.Horizontal(colors["num"], small_info.center(tw)))

    @classmethod
    def draw_logo(cls, colors):
        if cls.ACTIVE_LOGO is None:
            banners = [
                [
                    r"   _   _               _  ",
                    r"  | \ | |             (_) ",
                    r"  |  \| |  __ _ __ __ _   ",
                    r"  | . ` | / _` |\ \ / /| |",
                    r"  | |\  || (_| | \ V / | |",
                    r"  |_| \_| \__,_|  \_/  |_|",
                ],
                [
                    r"      ::::    :::     :::     :::     ::: ::::::::::: ",
                    r"     :+:+:   :+:   :+: :+:   :+:     :+:     :+:      ",
                    r"    :+:+:+  +:+  +:+   +:+  +:+     +:+     +:+       ",
                    r"   +#+ +:+ +#+ +#++:++#++: +#+     +:+     +#+        ",
                    r"  +#+  +#+#+# +#+     +#+  +#+   +#+      +#+         ",
                    r" #+#   #+#+# #+#     #+#   #+#+#+#       #+#          ",
                    r"###    #### ###     ###     ###     ###########       ",
                ],
                [
                    r"  _   _    _ __     _____ ",
                    r" | \ | |  / \ \   / /_ _|",
                    r" |  \| | / _ \ \ / / | | ",
                    r" | |\  |/ ___ \ V /  | | ",
                    r" |_| \_/_/   \_\_/  |___|",
                ]
            ]
            cls.ACTIVE_LOGO = random.choice(banners)

        logo_lines = cls.ACTIVE_LOGO
        tw = shutil.get_terminal_size().columns
        max_w = max(len(l) for l in logo_lines)
        offset = max(0, (tw - max_w) // 2)
        margin = " " * offset
        for line in logo_lines:
            print(Colorate.Horizontal(colors["banner"], margin + line))

        print()
        print(Colorate.Horizontal(colors["sub"], "~ PHÁT TRIỂN CÔNG CỤ, VÕ NHẬT HOÀNG ~".center(tw)))
        print()

    @classmethod
    def draw_dashboard(cls, active_idx):
        clr()
        colors = Theme.get_colors()
        box_w = cls.get_layout_width()
        margin = cls.get_margin(box_w)
        cls.draw_logo(colors)
        print()
        cls.draw_tabs(active_idx, colors, box_w, margin)
        print()
        cls.draw_page_content(active_idx, colors, box_w, margin)
        print()
        cls.draw_footer(colors, box_w, margin)

    @staticmethod
    def draw_card_box(title, items, theme_colors=None):
        colors = theme_colors or Theme.get_colors()
        tw = shutil.get_terminal_size().columns
        box_w = max(50, min(80, tw - 6))
        inner = box_w - 2
        margin = " " * max(0, (tw - box_w) // 2)

        border_len = max(2, (inner - len(title)) // 2)
        extra_dash = "─" if (inner - len(title)) % 2 != 0 else ""
        top_line = "┌" + "─" * border_len + title + "─" * border_len + extra_dash + "┐"
        if len(top_line) > box_w:
            top_line = top_line[:box_w - 1] + "┐"

        print()
        print(margin + Colorate.Horizontal(colors["head"], top_line))
        print(margin + Colorate.Horizontal(colors["num"], "│" + " " * inner + "│"))

        _items = list(items.items())
        col_w = (inner - 2) // 2

        for i in range(0, len(_items), 2):
            k1, v1 = _items[i]
            k2, v2 = _items[i + 1] if i + 1 < len(_items) else ("", "")

            max_v = col_w - len(k1) - 5
            val1 = (v1[:max_v - 3] + "...") if len(v1) > max_v else v1
            cell1 = f"  [{k1}] {val1:<{max_v}}"

            if k2:
                max_v2 = col_w - len(k2) - 5
                val2 = (v2[:max_v2 - 3] + "...") if len(v2) > max_v2 else v2
                cell2 = f"  [{k2}] {val2:<{max_v2}}"
            else:
                cell2 = " " * col_w

            plain_row = cell1 + cell2
            pad_right = max(0, inner - len(plain_row))
            colored_row = (
                Colorate.Horizontal(colors["num"], "│") +
                Colorate.Horizontal(colors["num"], f"  [{k1}]") +
                " " +
                Colorate.Horizontal(colors["txt"], f"{val1:<{max_v}}") +
                (
                    Colorate.Horizontal(colors["num"], f"  [{k2}]") +
                    " " +
                    Colorate.Horizontal(colors["txt"], f"{val2:<{max_v2}}")
                    if k2 else " " * col_w
                ) +
                " " * pad_right +
                Colorate.Horizontal(colors["num"], "│")
            )
            print(margin + colored_row)
        print(margin + Colorate.Horizontal(colors["num"], "│" + " " * inner + "│"))
        print(margin + Colorate.Horizontal(colors["head"], "└" + "─" * inner + "┘"))