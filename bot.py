# This Python file uses the following encoding: utf-8

import os
import sys
from android_auto_play_opencv import AapoManager

# Nox adbパス
ADB_PATH = "C:/Program Files/Nox/bin/"

# 斥候キャンプタップ位置
SCOUT_CAMP_TAP_POS = (800, 450)

aapo = None
template_dir_path = None


def main():
    global aapo, template_dir_path

    aapo = AapoManager(ADB_PATH)
    devices = aapo.adbl.devices

    for i, device in enumerate(devices):
        if device == "":
            continue
        print(f"{i + 1}: {device}")

    try:
        deviceNo = int(input("\n操作するNoxPlayerの番号を入力してください: "))
        device = devices[deviceNo - 1]
        aapo.adbl.setdevice(device)
    except:
        print("無効な入力値です。処理を中止します。")
        sys.exit(1)

    template_dir_path = os.path.join(os.path.dirname(__file__), "templates")

    print(f"\n===== 探索開始（CTRL+Cで終了） =====\n")

    auto_fog()


def auto_fog():
    while True:
        print(f"\n===== 派遣可能になるまで待機 =====\n")
        checkImg(os.path.join(template_dir_path, "scout_explore.png"), infinite=True)
        aapo.sleep(3)

        print(f"\n===== 霧選択 =====\n")
        try:
            checkImg(os.path.join(template_dir_path, "scout_explore.png"))
        except TimeoutError:
            goToScoutCamp()
            aapo.sleep(1)
            continue
        aapo.sleep(1)

        print(f"\n===== 斥候派遣 =====\n")
        try:
            checkImg(os.path.join(template_dir_path, "scout_send.png"))
        except TimeoutError:
            goToScoutCamp()
            aapo.sleep(1)
            continue
            
        aapo.sleep(1)
        goToScoutCamp()


def goToScoutCamp():
    print(f"\n===== 都市に戻る =====\n")
    checkImg(os.path.join(template_dir_path, "home.png"))
    aapo.sleep(5)
    print(f"\n===== 斥候キャンプ =====\n")
    aapo.touchPos(SCOUT_CAMP_TAP_POS[0], SCOUT_CAMP_TAP_POS[1])
    aapo.sleep(1)
    checkImg(os.path.join(template_dir_path, "scout.png"))


def checkImg(
    img_path: str,
    touch: bool = True,
    infinite: bool = False,
):
    timer = 0
    while True:
        aapo.screencap()
        result, x, y = aapo.chkImg2(img_path)

        if result:
            if touch:
                aapo.sleep(1)
                aapo.touchPos(x, y)
            break
        elif timer >= 9 and not infinite:
            raise TimeoutError
        else:
            timer += 1
            aapo.sleep(1)


if __name__ == "__main__":
    main()
