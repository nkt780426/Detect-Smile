Get-NetIPAddress | Where-Object {$_.AddressFamily -eq "IPv4" -and $_.PrefixLength -eq "24"} | Select-Object -ExpandProperty IPAddress

Nhược điểm: 
- Cười đau mặt mới tính là cười :))

------------------------------------------------------------------------------

Bước 1: Thiết lập
- Tải extension Tensorboard trên VSCode: không hiểu thì xem tại https://stackoverflow.com/questions/63938552/how-to-run-tensorboard-in-vscode
- Tải dataset vào thư mục gốc của project và đặt tên chính xác là "dataset"
- Cài đặt các package trong requirements.txt: pip install -r requirements.txt
=> Bản thân tôi phải cài Ubuntu dual boot với Windows nên có thể Tensorboard sẽ không nhìn thấy hoặc cấu hình khác, tra ChatGPT để biết thông tin chi tiết
Dùng Ubuntu nhanh hơn WSL2 nhiều, tôi train 20 phút được 11 epoch, trong khi WSL2 thì lâu lắm

Bước 2: Vấn đề tồn đọng
- Ở bước cuối evaluate: Phải vẽ được ROC bằng Pylot để xác định threshold cho phù hợp (không hiểu đoạn này hỏi lại tôi)
- Chưa code lại file OpenCV để đếm số khuôn mặt cười

pip install flask

https://learn.microsoft.com/en-us/windows/wsl/connect-usb