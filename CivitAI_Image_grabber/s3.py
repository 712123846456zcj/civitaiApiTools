import os
print("\n注意：Tag search 模式\n")
ss=input("【+】请输入你的大写tag：")
os.system(f"""python civit_image_downloader.py --timeout=60  --quality=1 --redownload=2  --mode=3   --tags="{ss}"  --disable_prompt_check=n""")
