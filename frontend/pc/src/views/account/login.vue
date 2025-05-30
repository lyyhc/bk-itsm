<template>
  <div class="login-page">
    <transition name="fade-slide">
      <div class="glass-card" v-show="showCard">
        <h2 class="title">ITSM 系统登录</h2>
        <form @submit.prevent="handleLogin" class="login-form">
          <div class="input-group">
            <label>用户名</label>
            <input v-model="username" required placeholder="请输入用户名" />
          </div>
          <div class="input-group">
            <label>密码</label>
            <input type="password" v-model="password" required placeholder="请输入密码" />
          </div>
          <button type="submit" class="login-btn ripple">登录</button>
          <p v-if="errorMessage" class="error-msg">{{ errorMessage }}</p>
        </form>
      </div>
    </transition>
  </div>
</template>

<script>
  import axios from 'axios';

  export default {
    name: 'Login',
    data() {
      return {
        username: '',
        password: '',
        errorMessage: '',
        showCard: false,
      };
    },
    mounted() {
      setTimeout(() => {
        this.showCard = true;
      }, 200);
    },
    methods: {
      async handleLogin() {
        try {
          const res = await axios.post('/api/account/token/', {
            username: this.username,
            password: this.password,
          });
          const { access, refresh } = res.data;
          localStorage.setItem('access_token', access);
          localStorage.setItem('refresh_token', refresh);
          // axios.defaults.headers.Authorization = `Bearer ${access}`;
          // axios.defaults.headers.common.Authorization = `Bearer ${access}`;
          window.location.reload();
        } catch (err) {
          this.errorMessage = '登录失败，请检查用户名或密码';
        }
      },
    },
  };
</script>

<style scoped>
.login-page {
  height: 100vh;
  background: linear-gradient(120deg, #0f2027, #203a43, #2c5364);
  background-size: 400% 400%;
  animation: gradientBG 15s ease infinite;
  display: flex;
  justify-content: center;
  align-items: center;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  overflow: hidden;
}

@keyframes gradientBG {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}

.glass-card {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border-radius: 16px;
  padding: 40px 30px;
  box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
  width: 360px;
  color: white;
}

.title {
  text-align: center;
  margin-bottom: 25px;
  font-size: 24px;
  letter-spacing: 1px;
}

.login-form .input-group {
  margin-bottom: 20px;
  display: flex;
  flex-direction: column;
}

.input-group label {
  margin-bottom: 6px;
  font-size: 14px;
}

.input-group input {
  padding: 10px 12px;
  border: none;
  border-radius: 8px;
  background-color: rgba(255, 255, 255, 0.2);
  color: white;
  transition: all 0.3s ease;
}

.input-group input::placeholder {
  color: rgba(255, 255, 255, 0.5);
}

.input-group input:focus {
  outline: none;
  background-color: rgba(255, 255, 255, 0.3);
  transform: scale(1.02);
}

.login-btn {
  width: 100%;
  padding: 12px;
  border: none;
  border-radius: 8px;
  background: linear-gradient(45deg, #00d2ff, #3a7bd5);
  color: white;
  font-weight: bold;
  cursor: pointer;
  overflow: hidden;
  position: relative;
  z-index: 1;
}

.login-btn:hover {
  background: linear-gradient(45deg, #3a7bd5, #00d2ff);
}

/* 按钮点击涟漪动画 */
.login-btn::after {
  content: "";
  position: absolute;
  background: rgba(255, 255, 255, 0.5);
  border-radius: 50%;
  transform: scale(0);
  opacity: 0;
  transition: transform 0.6s, opacity 0.8s;
  pointer-events: none;
  z-index: 0;
}

.login-btn:active::after {
  transform: scale(4);
  opacity: 1;
  transition: 0s;
}

.login-btn.ripple:active::after {
  top: 50%;
  left: 50%;
  width: 100px;
  height: 100px;
  margin-left: -50px;
  margin-top: -50px;
}

/* 错误信息 */
.error-msg {
  margin-top: 10px;
  color: #ff6b6b;
  text-align: center;
}

/* 动画：面板滑入 + 淡入 */
.fade-slide-enter-active {
  animation: slideInUp 0.8s ease;
}
.fade-slide-leave-active {
  animation: slideOutDown 0.8s ease;
}
@keyframes slideInUp {
  from {
    transform: translateY(80px);
    opacity: 0;
  }
  to {
    transform: translateY(0);
    opacity: 1;
  }
}
@keyframes slideOutDown {
  from {
    transform: translateY(0);
    opacity: 1;
  }
  to {
    transform: translateY(80px);
    opacity: 0;
  }
}
</style>
