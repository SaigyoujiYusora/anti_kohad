import os
import random
import hoshino
from hoshino import Service, priv, R
from hoshino.config import RES_DIR
from hoshino.typing import CQEvent

# sv = Service('anti-KohaD', enable_on_default=False,manage_priv=priv.ADMIN)
sv = Service(
    name='anti-KohaD',  # 功能名
    use_priv=priv.NORMAL,  # 使用权限
    manage_priv=priv.ADMIN,  # 管理权限
    visible=True,  # 可见性
    enable_on_default=True,  # 默认启用
    bundle='娱乐',  # 分组归类
    # help_ = sv_help #帮助说明
)
imgpath = os.path.join(os.path.expanduser(RES_DIR), 'img', 'kohad')
pandoraimgpath = os.path.join(os.path.expanduser(RES_DIR), 'img', 'kohad', 'maimai')

QRCODE_RECALL_MSG_TIME = 45

kohad = '''
kohad KohaD KOHAD 弱虫 麒麟 秒针 39 100块 一百块 潘 潘多拉 白潘 8em 8EM 8-em 紅蓮華 MIRACLE RUSH Pretender 红莲华 loser LOSER usa
USA u.s.a. U.S.A. 你不知道的故事 君の知らない物語 物語 物语 咬住秒针 秒針を噛む ArtyParty 
'''


@sv.on_keyword(kohad)
# @sv.on_rex(r'(嘉[\.\s]*(然|人))|(嘉[\.\s]*心[\.\s]*糖)')
async def anti_kohad(bot, ev: CQEvent):
    kohad_img = "shanle.jpg"
    ruochong_img = "ruochong.jpg"
    S100_img = "100kuai.jpg"
    pandora_img = random.choice(os.listdir(pandoraimgpath))
    eight_em_img = "8em.jpg"

    ranum = random.random()

    if '39music' in ev.message.extract_plain_text():
        pass
    elif '弱虫' in ev.message.extract_plain_text():
        try:
            sentimg = R.img(f'kohad/{ruochong_img}').cqcode
        except Exception as e:
            hoshino.logger.error(f'读取弱虫梗图时发生错误{type(e)}')
        await bot.send(ev, sentimg)
    elif ('一百块' or '100块') in ev.message.extract_plain_text():
        try:
            sentimg = R.img(f'kohad/{S100_img}').cqcode
        except Exception as e:
            hoshino.logger.error(f'读取一百块梗图时发生错误{type(e)}')
        await bot.send(ev, sentimg)
    elif ('潘' or '潘多拉' or '白潘') in ev.message.extract_plain_text():
        try:
            sentimg = R.img(f'kohad/pan/{pandora_img}').cqcode
        except Exception as e:
            hoshino.logger.error(f'读取潘梗图时发生错误{type(e)}')
        await bot.send(ev, sentimg)
    elif ('8em' or '8EM' or '8-em') in ev.message.extract_plain_text():
        try:
            sentimg = R.img(f'kohad/{eight_em_img}').cqcode
        except Exception as e:
            hoshino.logger.error(f'读取8em梗图时发生错误{type(e)}')
        await bot.send(ev, sentimg)
    else:
        try:
            sentimg = R.img(f'kohad/{kohad_img}').cqcode
        except Exception as e:
            hoshino.logger.error(f'读取KohaD弔图时发生错误{type(e)}')
        await bot.send(ev, sentimg)
    hoshino.logger.info(f'anti_kohad随机数为{ranum}')



