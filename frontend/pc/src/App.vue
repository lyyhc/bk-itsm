<template>
  <component :is="isAuthenticated ? 'MainApp' : 'LoginView'" />
</template>

<script>
  import MainApp from './MainApp.vue';
  import LoginView from './views/account/login.vue';

  export default {
    name: 'App',
    components: {
      MainApp,
      LoginView,
    },
    computed: {
      isAuthenticated() {
        return !!localStorage.getItem('access_token');
      },
    },
  };
</script>

