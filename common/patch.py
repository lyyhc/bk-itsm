from rest_framework_simplejwt.backends import TokenBackend
import jwt


def patch_simplejwt_tokenbackend():

    def fixed_encode(self, payload):
        headers = getattr(self, 'headers', None)
        # 调用 PyJWT 2.x encode 返回字符串，无需 decode
        token = jwt.encode(
            payload,
            self.signing_key,
            algorithm=self.algorithm,
            headers=headers,
        )
        return token  # 直接返回字符串，不做 decode

    TokenBackend.encode = fixed_encode
