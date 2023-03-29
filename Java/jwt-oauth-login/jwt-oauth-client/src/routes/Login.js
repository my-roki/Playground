import utils from "../utils.js";
import styled from "./Login.module.css";

const socials = [
  {
    socialType: "google",
    src: utils.getSocialImage("google"),
    comment: "구글 로그인",
  },
  {
    socialType: "facebook",
    src: utils.getSocialImage("facebook"),
    comment: "페이스북 로그인",
  },
  {
    socialType: "naver",
    src: utils.getSocialImage("naver"),
    comment: "네이버 로그인",
  },
  {
    socialType: "kakao",
    src: utils.getSocialImage("kakao"),
    comment: "카카오 로그인",
  },
];

function Login() {
  return (
    <div className={styled.container}>
      <div>
        <h4>로그인</h4>
      </div>
      <div className={styled.loginContainer}>
        <div className={styled.socialContainer}>
          {socials.map((social) => {
            return (
              <a className={styled.socialButton} href={utils.getSocialLoginUrl(social.socialType)}>
                <img className={styled.socialImage} src={social.src} alt="social icon"/>
                {social.comment}
              </a>
            );
          })}
        </div>
      </div>
    </div>
  );
}

export default Login;
