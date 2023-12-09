<template>
  <q-layout class="row justify-center items-center" style="min-height: 600px">
    <q-page-container style="min-width: 30%">
      <q-card class="my-card q-pa-md" style="background: var(--chamRed)">
        <q-card-section class="q-pb-none">
          <div class="text-h5 text-center q-mb-md">Sign Up</div>
          <q-form @submit.prevent="onSubmit">
            <q-input
              class="q-my-sm"
              filled
              v-model="userInfo.firstname"
              label="First Name"
              lazy-rules
              :rules="[
                (val) =>
                  (val && val.length > 0) || 'Please enter your first name',
              ]"
            />
            <q-input
              class="q-my-sm"
              filled
              v-model="userInfo.lastname"
              label="Last Name"
              lazy-rules
              :rules="[
                (val) =>
                  (val && val.length > 0) || 'Please enter your last name',
              ]"
            />
            <q-input
              class="q-my-sm"
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
              class="q-my-sm"
              filled
              v-model="userInfo.phone"
              label="Phone Number"
              lazy-rules
              :rules="[
                (val) =>
                  (val && val.length > 0) || 'Please enter your phone number',
                (val) =>
                  /^\d{10}$/.test(val) ||
                  'Please enter a valid 10-digit phone number',
              ]"
            />
            <q-input
              class="q-my-sm"
              filled
              v-model="userInfo.address"
              label="Address"
              lazy-rules
              :rules="[
                (val) => (val && val.length > 0) || 'Please enter your address'
              ]"
            />
            <q-input
              class="q-my-sm"
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
            <q-input
              class="q-my-sm"
              filled
              v-model="userInfo.confirmPassword"
              type="password"
              label="Confirm Password"
              lazy-rules
              :rules="[
                (val) => val === userInfo.password || 'Passwords do not match',
              ]"
            />

            <div class="q-mt-md">
              <q-btn label="Register" type="submit" class="blue-btn btn-size" stretch :disabled="loading"/>
            </div>
          </q-form>
        </q-card-section>

        <q-card-section>
          <div class="row justify-center q-my-md">
            <q-btn
              flat
              label="Already have an account? Login"
              class="green-btn"
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
    const userInfo = ref({
      firstname: "",
      lastname: "",
      username: "",
      phone: "",
      address: "",
      password: "",
      confirmPassword: "",
    });

    const router = useRouter();
    const loading = ref(false);

    async function onSubmit() {
      console.log(userInfo.value);
      try {
        loading.value = true;
        const response = await axios.post(
          "http://localhost:8000/register",
          userInfo.value
        );
        console.log(response);
        router.push("/login");
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

    function goToLogin() {
      router.push("/login");
    }

    return {
      userInfo,
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
