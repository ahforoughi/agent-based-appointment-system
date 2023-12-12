<template>
  <q-layout
    class="row justify-center items-center q-pa-md"
    style="min-height: 70vh"
  >
    <q-page-container style="min-width: 30%">
      <q-card class="my-card q-pa-md" style="background: var(--honeyDoo)">
        <q-card-section class="q-mt-l">
          <div class="text-h5 text-center q-my-lg text-weight-bold">Login</div>
          <q-form @submit.prevent="onLogin">
            <q-input
              class="q-mb-md"
              filled
              v-model="userInfo.username"
              label="UCalgary Email"
              lazy-rules
              :rules="[
                (val) => (val && val.length > 0) || 'Please enter your email',
                (val) =>
                  /^\S+@\S+\.\S+$/.test(val) || 'Please enter a valid email',
                (val) =>
                  (val && val.endsWith('@ucalgary.ca')) ||
                  'Please enter a UCalgary email',
              ]"
            />
            <q-input
              class="q-mb-md"
              filled
              v-model="userInfo.password"
              type="password"
              label="Password"
              lazy-rules
              :rules="[
                (val) =>
                  (val && val.length > 5) ||
                  'Password should be more than 5 characters',
              ]"
            />
            <div class="q-mt-md">
              <q-btn
                label="Login"
                type="submit"
                class="green-btn btn-size"
                stretch
                :disabled="loading"
              />
            </div>
          </q-form>
        </q-card-section>

        <q-card-section>
          <div class="row justify-center q-mb-md">
            <q-btn
              flat
              label="New here? Sign up"
              class="q-px-lg blue-btn"
              @click="goToRegister"
            />
          </div>
        </q-card-section>
      </q-card>
    </q-page-container>
  </q-layout>
</template>

<script>
import axios from "axios";
import { ref, inject } from "vue";
import { useRouter } from "vue-router";
import { Notify } from "quasar";

export default {
  setup() {
    const userInfo = ref({
      username: "",
      password: "",
    });
    const loading = ref(false);

    const sharedState = inject("sharedState");
    const router = useRouter();

    async function onLogin() {
      console.log(userInfo.value);
      loading.value = true;
      try {
        const response = await axios.post(
          "http://localhost:9000/login",
          userInfo.value
        );
        console.log(response);
        sharedState.isUserLoggedIn = true;
        sharedState.username = response.data.user_info.username;
        sharedState.firstname = response.data.user_info.firstname;
        sharedState.lastname = response.data.user_info.lastname;
        sharedState.phone = response.data.user_info.phone;
        localStorage.setItem("isUserLoggedIn", true);
        localStorage.setItem("username", response.data.user_info.username);
        localStorage.setItem("firstname", response.data.user_info.firstname);
        localStorage.setItem("lastname", response.data.user_info.lastname);
        localStorage.setItem("phone", response.data.user_info.phone);
        router.push("/user");
      } catch (error) {
        console.error("There was an error!", error);
        Notify.create({
          color: "red-4",
          message: "Please try again!",
          icon: "error",
          position: "center",
          classes: "q-py-md q-px-lg",
        });
      } finally {
        loading.value = false;
      }
    }

    function goToRegister() {
      router.push("/register");
    }

    return {
      userInfo,
      onLogin,
      goToRegister,
      loading,
    };
  },
};
</script>

<style scoped>
.my-card {
  border-radius: 25px;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1),
    0 2px 4px -1px rgba(0, 0, 0, 0.06);
}
</style>
