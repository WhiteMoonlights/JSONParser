import json
import re
import jsonpath
from log.log_config import GetLogger


class ResponseExtractor:
    def main(self, res_text, expr):
        r = self.jsonpath_extractor(res_text, expr)
        if r:
            return r
        else:
            r = self.re_extractor(res_text, expr)
            if not r:
                r = False
                GetLogger().error(f"未根据JSONPATH或正则表达式【{expr}】获取到匹配结果")
            return r

    def jsonpath_extractor(self, res_text, expr):
        try:
            res_text = json.loads(res_text)
        except:
            GetLogger().debug(f"未通过JSONPATH获取到匹配结果，JSONPATH:【{expr}】,响应结果【{res_text}】")
        else:
            r = jsonpath.jsonpath(res_text, expr)
            if r:
                GetLogger().debug(f"成功通过JSONPATH{expr}获取到匹配结果:{r[0]}")
            elif expr == "$":
                r = [res_text]
            else:
                GetLogger().debug(f"未通过JSONPATH获取到匹配结果，JSONPATH:【{expr}】")
            return r

    def re_extractor(self, res_text, expr):
        try:
            r = re.findall(expr, res_text)
            if r:
                GetLogger().debug(f"成功通过正则表达式【{expr}】获取到匹配结果:{r[0]}")
                return r[0]
            else:
                GetLogger().debug(f"未通过正则表达式【{expr}】匹配到结果")
                return r
        except:
            GetLogger().debug(f"未通过正则表达式【{expr}】匹配到结果")


if __name__ == '__main__':
    r = '{"user.default.password": "123","web": "DEFAULT","permission.type": "ROLE"}'
    expr = 'password\\": \\"(\\w*)\\"'
    # expr = "$"
    r = ResponseExtractor().main(r, expr)
    print(r)
