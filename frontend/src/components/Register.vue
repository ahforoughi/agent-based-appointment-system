<template>
  <q-layout
    class="row justify-center items-center q-pa-md"
    style="min-height: 80vh"
  >
    <q-page-container>
      <q-card class="my-card q-pa-md" style="max-width: 400px">
        <q-card-section class="q-pb-none">
          <div class="text-h5 text-center q-mb-md">Sign Up</div>
          <q-form @submit.prevent="onSubmit">
            <q-input
              filled
              v-model="user.name"
              label="Full Name"
              lazy-rules
              :rules="[
                (val) =>
                  (val && val.length > 0) || 'Please enter your full name',
              ]"
            />
            <q-input
              filled
              v-model="user.email"
              label="Email"
              lazy-rules
              :rules="[
                (val) => (val && val.length > 0) || 'Please enter your email',
                (val) =>
                  /^\S+@\S+\.\S+$/.test(val) || 'Please enter a valid email',
              ]"
            />
            <q-input
              filled
              v-model="user.password"
              type="password"
              label="Password"
              lazy-rules
              :rules="[
                (val) =>
                  (val && val.length > 5) ||
                  'Password should be more than 5 characters',
              ]"
            />
            <q-input
              filled
              v-model="user.confirmPassword"
              type="password"
              label="Confirm Password"
              lazy-rules
              :rules="[
                (val) => val === user.password || 'Passwords do not match',
              ]"
            />

            <div class="q-mt-md">
              <q-btn label="Register" type="submit" color="primary" stretch :disabled="loading"/>
            </div>
          </q-form>
        </q-card-section>

        <q-card-section>
          <div class="row justify-center q-mt-md">
            <q-btn
              flat
              label="Already have an account? Login"
              color="primary"
              @click="goToLogin"
            />
          </div>
        </q-card-section>
      </q-card>
    </q-page-container>
  </q-layout>
</template>

<script>
import { ref } from "vue";
import { useRouter } from "vue-router";
import axios from "axios";
import { Notify } from "quasar";

export default {
  setup() {
    const user = ref({
      name: "",
      email: "",
      password: "",
      confirmPassword: "",
    });

    const router = useRouter();
    const loading = ref(false);

    async function onSubmit() {
      const userInfo = {
        username: "zahra.arabi",
        phone: "3681111111",
        password: "password",
        email: "zahraarabi@ucalgary.ca",
      };

      try {
        loading.value = true;
        const response = await axios.post("http://localhost:8000/register", userInfo);
        console.log(response);
        router.push("/login");
      } catch (error) {
        console.error("There was an error!", error);
        Notify.create({
          color: "negative",
          message: "Please try again!",
          icon: "error",
        });
      } finally {
        loading.value = false;
      }
    }

    function goToLogin() {
      router.push("/login");
    }

    return {
      user,
      loading,
      onSubmit,
      goToLogin,
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
