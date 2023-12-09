<script setup>
</script>

<template>
  <q-layout>
    <q-header
      elevated
      style="background: var(--airBlue); height: 10vh; display: flex"
    >
      <q-toolbar>
        <q-btn flat dense round icon="home" to="/" style="margin-left: 5px; font-size: 1.1rem" />
        <q-toolbar-title style="margin-left: 20px; text-align: left">
          <q-avatar size="2.5rem">
            <img src="@/assets/logo-1.1.png" alt="logo" />
          </q-avatar>
          WellBookUofC
        </q-toolbar-title>

        <q-space />

        <div style="margin-right: 40px">
          <router-link
            v-if="sharedState.isUserLoggedIn"
            to="/user"
            class="avatar-link"
          >
            <q-avatar size="2.5rem">
            <img src="@/assets/user.jpeg" alt="logo" />
          </q-avatar>
          </router-link>
        </div>
      </q-toolbar>
    </q-header>

    <div style="padding: 15vh 0">
      <router-view />
    </div>

    <q-footer
      elevated
      style="background: var(--salmonPink); height: 8vh; display: flex"
    >
      <q-toolbar class="justify-center">
        <p style="display: inline-block" class="q-my-auto">
          &copy; 2023 Student Wellness Services Booking Website. All rights
          reserved.
        </p>
        <q-btn class="q-mx-lg light-red-btn btn-size" label="About Us" @click="open()" />

        <q-dialog v-model="dialog">
          <q-card class="my-card" style="min-width: 600px">
            <q-img src="@/assets/logo-18.6.jpg" :ratio="18 / 6" />

            <q-card-section>
              <div class="row no-wrap items-center">
                <div class="col text-h5 ellipsis text-bold">WellBookUofC</div>
              </div>
            </q-card-section>

            <q-card-section class="q-pt-none">
              <div class="text-subtitle1">
                Hey there! We're Group 7, a team of ESE students working on an
                appointment booking system for the University of Calgary
                wellness center. Meet our group members:
              </div>
              <div>
                <q-item clickable v-ripple>
                  <q-item-section avatar>
                    <q-avatar>
                      <img src="@/assets/long-hair.png" />
                    </q-avatar>
                  </q-item-section>
                  <q-item-section>Mahboobe Shakeri</q-item-section>
                </q-item>
                <q-item clickable v-ripple>
                  <q-item-section avatar>
                    <q-avatar>
                      <img src="@/assets/curly-hair.png" />
                    </q-avatar>
                  </q-item-section>
                  <q-item-section>Zahra Arabi</q-item-section>
                </q-item>
                <q-item clickable v-ripple>
                  <q-item-section avatar>
                    <q-avatar>
                      <img src="@/assets/short-hair.png" />
                    </q-avatar>
                  </q-item-section>
                  <q-item-section>Sara Montajab</q-item-section>
                </q-item>
                <q-item clickable v-ripple>
                  <q-item-section avatar>
                    <q-avatar>
                      <img src="@/assets/businessman.png" />
                    </q-avatar>
                  </q-item-section>
                  <q-item-section>Amirhossein Foroughi</q-item-section>
                </q-item>
              </div>
            </q-card-section>

            <q-separator />
          </q-card>
        </q-dialog>
      </q-toolbar>
    </q-footer>
  </q-layout>
</template>

<script>
import { ref, reactive, provide } from "vue";
// import axios from "axios";

export default {
  setup() {
    const dialog = ref(false);
    const position = ref("bottom");

    const sharedState = reactive({
      isUserLoggedIn: localStorage.getItem("isUserLoggedIn")
        ? localStorage.getItem("isUserLoggedIn")
        : false,
    });

    provide("sharedState", sharedState);
    console.log(localStorage.getItem("isUserLoggedIn"));

    // async function fetchData() {
    //   try {
    //     const response = await axios.get("http://localhost:8000/");
    //     console.log(response);
    //   } catch (error) {
    //     console.error("There was an error!", error);
    //   }
    // }

    return {
      dialog,
      position,
      sharedState,

      open() {
        dialog.value = true;
      },
    };
  },
};
</script>

<style scoped>
.footer {
  width: 100%;
  background-color: #d2e7ea;
  padding: 10px;
  text-align: center;
  height: 10vh;
}
.avatar-link {
  color: inherit;
  text-decoration: none;
}
</style>
