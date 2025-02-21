import os
print("\n注意：是模型 ID 模式\n")
ss=input("【+】请输入你的模型id：")
os.system(f"python civit_image_downloader.py --timeout=60  --quality=1 --redownload=2  --mode=2   --model_id={ss}")
