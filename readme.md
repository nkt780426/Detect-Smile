Get-NetIPAddress | Where-Object {$_.AddressFamily -eq "IPv4" -and $_.PrefixLength -eq "24"} | Select-Object -ExpandProperty IPAddress

Nhược điểm: 
- Cười đau mặt mới tính là cười :))

------------------------------------------------------------------------------

- Frame => haar_casscade => x,y,z,t => Ma trận 2 chiều hoặc 3 chiều
- Input: (None, 64, 64, 3) => None là batch_sise
    roi_bgr = np.expand_dims(roi_bgr, axis=0)  # Thêm chiều batch
- Ảnh phải về màu xám
- Chuẩn hóa chia 255

-------------------------------------------------------------------------------
sudo apt-get update
sudo apt-get install qtbase5-dev
sudo apt-get install -y libgtk2.0-dev pkg-config
sudo apt-get install -y libcanberra-gtk-module
pip uninstall opencv-python opencv-python-headless
pip install opencv-python