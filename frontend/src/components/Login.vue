<template>
<q-layout class="row justify-center items-center q-pa-md" style="min-height: 80vh">
  <q-page-container >
    <q-card class="my-card q-pa-md" style="width: 400px;">
      <q-card-section class="q-pb-none">
        <div class="text-h5 text-center q-mb-md">Login</div>
        <q-form @submit.prevent="onLogin">
          <q-input filled v-model="loginInfo.email" label="Email" lazy-rules :rules="[ val => val && val.length > 0 || 'Please enter your email']" />
          <q-input filled v-model="loginInfo.password" type="password" label="Password" lazy-rules :rules="[ val => val && val.length > 5 || 'Password should be more than 5 characters']" />

          <div class="q-mt-md">
            <q-btn label="Login" type="submit" color="primary" stretch />
          </div>
        </q-form>
      </q-card-section>

      <q-card-section>
        <div class="row justify-center q-mt-md">
          <q-btn flat label="New here? Sign up" color="primary" @click="goToRegister" />
        </div>
      </q-card-section>
    </q-card>
  </q-page-container>
  </q-layout>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const loginInfo = ref({
  email: '',
  password: ''
})

const router = useRouter()

function onLogin() {
  console.log('Logging in:', loginInfo.value)
}

function goToRegister() {
  router.push('/register')
}
</script>

<style scoped>
.my-card {
  border-radius: 25px;
  box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1), 0 2px 4px -1px rgba(0,0,0,0.06);
}
</style>
