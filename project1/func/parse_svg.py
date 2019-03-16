def parse_num(text):
    a = text
    a = a.replace('<span class="', "")
    a = a.replace('"></span>', "")
    a = a.replace('<b>', "")
    a = a.replace('</b>', "")
    a = a.replace('xwu7jk', "0")
    a = a.replace('xwu3rz', "2")
    a = a.replace('xwua88', "3")
    a = a.replace('xwux4c', "4")
    a = a.replace('xwucnz', "5")
    a = a.replace('xwuox3', "6")
    a = a.replace('xwu626', "7")
    a = a.replace('xwufmm', "8")
    a = a.replace('xwuw8j', "9")  
    # type: str
    return a

def parse_food_type(text):
    a = text
    a = a.replace('<span class="tag">', "")
    a = a.replace('<span class="', "")
    a = a.replace('"></span>', "")
    a = a.replace('</span>', "")
    # 小吃快餐
    a = a.replace('kkcv6i', "小")
    a = a.replace('kkcp6e', "吃")
    a = a.replace('kkcdou', "快")
    a = a.replace('kkc1nq', "餐")
    # 面包甜点
    a = a.replace('kkc3y9', "面")
    a = a.replace('kkchx8', "包")
    a = a.replace('kkcgan', "甜")
    a = a.replace('kkcrd6', "点")
    # 粤菜
    a = a.replace('kkcazw', "菜")
    # 自助餐
    a = a.replace('kkcrwr', "自")
    a = a.replace('kkc2h2', "助")
    a = a.replace('kkc1nq', "餐")
    # 日本菜
    a = a.replace('kkc74y', "日")
    a = a.replace('kkcbif', "本")
    # 火锅
    a = a.replace('kkcm3c', "火")
    a = a.replace('kkcccp', "锅")
    # 西餐
    a = a.replace('kkcg98', "西")
    # 小龙虾
    a = a.replace('kkcv6i', "小")
    a = a.replace('kkck38', "龙")
    a = a.replace('kkcrex', "虾")
    # 江河湖海鲜
    a = a.replace('kkcenl', "江")
    a = a.replace('kkcpc1', "河")
    a = a.replace('kkcf21', "湖")
    a = a.replace('kkcsmk', "海")
    a = a.replace('kkcdd1', "鲜")
    # 烧烤
    a = a.replace('kkciz4', "烧")
    a = a.replace('kkcksq', "烤")
    # 韩国料理
    a = a.replace('kkc5ow', "国")
    a = a.replace('kkcze5', "料")
    a = a.replace('kkcbsw', "理")
    # 川菜
    a = a.replace('kkc97t', "川")
    # 饮品店
    a = a.replace('kkclf0', "饮")
    a = a.replace('kkc5o4', "品")
    a = a.replace('kkch1f', "店")
    # 粥粉面
    a = a.replace('kkcccj', "粥")
    a = a.replace('kkc7qt', "粉")
    a = a.replace('kkc3y9', "面")
    # 水果生鲜
    a = a.replace('kkcv9q', "水")
    a = a.replace('kkc9qv', "果")
    a = a.replace('kkcyd3', "生")
    a = a.replace('kkcdd1', "鲜")
    # 食品保健
    a = a.replace('kkc681', "食")
    a = a.replace('kkc5o4', "品")
    a = a.replace('kkcw9j', "保")
    a = a.replace('kkcp9h', "健")
    # 茶餐厅
    a = a.replace('kkcg6m', "茶")
    a = a.replace('kkc1nq', "餐")
    a = a.replace('kkcn75', "厅")
    # 东北菜
    a = a.replace('kkc0f7', "东")
    a = a.replace('kkcyk4', "北")
    a = a.replace('kkcazw', "菜")
    # 私房菜
    a = a.replace('kkc8j1', "私")
    a = a.replace('kkc7jf', "房")
    a = a.replace('kkcazw', "菜")
    # 本帮江浙菜
    a = a.replace('kkcbif', "本")
    a = a.replace('kkc3w8', "帮")
    a = a.replace('kkcenl', "江")
    a = a.replace('kkc5of', "浙")
    a = a.replace('kkcazw', "菜")
    # 西北菜
    a = a.replace('kkcg98', "西")
    a = a.replace('kkcyk4', "北")
    a = a.replace('kkcazw', "菜")
    # 东南亚菜
    a = a.replace('kkc0f7', "东")
    a = a.replace('kkcs60', "南")
    a = a.replace('kkcrp4', "亚")
    a = a.replace('kkcazw', "菜")
    # 农家菜
    a = a.replace('kkco1l', "农")
    a = a.replace('kkcrhp', "家")
    a = a.replace('kkcazw', "菜")
    # 家常菜
    a = a.replace('kkcrhp', "家")
    a = a.replace('kkccw1', "常")
    a = a.replace('kkcazw', "菜")
    # 创意菜
    a = a.replace('kkcllu', "创")
    a = a.replace('kkcd76', "意")
    a = a.replace('kkcazw', "菜")
    # 北京菜
    a = a.replace('kkcyk4', "北")
    a = a.replace('kkcexo', "京")
    a = a.replace('kkcazw', "菜")
    # 素菜
    a = a.replace('kkckqx', "素")
    a = a.replace('kkcazw', "菜")
    # 云贵菜
    a = a.replace('kkcfat', "云")
    a = a.replace('kkc225', "贵")
    a = a.replace('kkcazw', "菜")
    # 新疆菜
    a = a.replace('kkciz2', "新")
    a = a.replace('kkc7dr', "疆")
    a = a.replace('kkcazw', "菜")
    # 台湾菜
    a = a.replace('kkcvoz', "台")
    a = a.replace('kkc5r3', "湾")
    a = a.replace('kkcazw', "菜")
    # 福建菜
    a = a.replace('kkcwpu', "福")
    a = a.replace('kkciw5', "建")
    a = a.replace('kkcazw', "菜")
    # 其他美食
    a = a.replace('kkcezn', "其")
    a = a.replace('kkcq7j', "他")
    a = a.replace('kkcq8v', "美")
    a = a.replace('kkc681', "食")  
    # type: str
    return a

def parse_location(text):
    a = text
    a = a.replace('<span class="tag">', "")
    a = a.replace('<span class="', "")
    a = a.replace('"></span>', "")
    a = a.replace('</span>', "")
    # 市中心区
    a = a.replace('kkciug', "市")
    a = a.replace('kkcdsg', "中")
    a = a.replace('kkcer9', "心")
    a = a.replace('kkc254', "区")
    # 车公庙
    a = a.replace('kkcxsj', "车")
    a = a.replace('kkc1kc', "公")
    a = a.replace('kkc9no', "庙")
    # 上沙/下沙
    a = a.replace('kkc4wp', "上")
    a = a.replace('kkczcu', "沙")
    a = a.replace('kkcx4w', "下")
    a = a.replace('kkczcu', "沙")
    # 梅林
    a = a.replace('kkczeh', "梅")
    a = a.replace('kkcux5', "林")
    # 华强北
    a = a.replace('kkczrb', "华")
    a = a.replace('kkc6rw', "强")
    a = a.replace('kkcyk4', "北")
    # 皇岗
    a = a.replace('kkc8hk', "皇")
    a = a.replace('kkcdpw', "岗")
    # 景田
    a = a.replace('kkc5rk', "景")
    a = a.replace('kkc0m7', "田")
    # 新洲
    a = a.replace('kkciz2', "新")
    a = a.replace('kkcd7s', "洲")
    # 香蜜湖
    a = a.replace('kkc07j', "香")
    a = a.replace('kkck6t', "蜜")
    a = a.replace('kkcf21', "湖")
    # 荔枝公园片区
    a = a.replace('kkchzp', "枝")
    a = a.replace('kkc1kc', "公")
    a = a.replace('kkc554', "园")
    a = a.replace('kkc478', "片")
    a = a.replace('kkc254', "区")
    # 石厦
    a = a.replace('kkcyqw', "石")
    a = a.replace('kkcrm3', "厦")
    # 八卦岭/园岭
    a = a.replace('kkctuk', "八")
    a = a.replace('kkc6ij', "岭")
    a = a.replace('kkc554', "园")
    a = a.replace('kkc6ij', "岭")
    # 竹子林
    a = a.replace('kkc47i', "竹")
    a = a.replace('kkc7s2', "子")
    a = a.replace('kkcux5', "林")
    # 市民中心
    a = a.replace('kkciug', "市")
    a = a.replace('kkcbfi', "民")
    a = a.replace('kkcdsg', "中")
    a = a.replace('kkcer9', "心")
    # 华强南
    a = a.replace('kkczrb', "华")
    a = a.replace('kkc6rw', "强")
    a = a.replace('kkcs60', "南")
    # 岗厦
    a = a.replace('kkcdpw', "岗")
    a = a.replace('kkcrm3', "厦")
    # 福田保税区
    a = a.replace('kkcwpu', "福")
    a = a.replace('kkc0m7', "田")
    a = a.replace('kkcw9j', "保")
    a = a.replace('kkcjv6', "税")
    a = a.replace('kkc254', "区")
    # 沙头
    a = a.replace('kkczcu', "沙")
    a = a.replace('kkcw4t', "头") 
    # type: str
    return a
