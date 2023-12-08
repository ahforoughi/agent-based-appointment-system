<script setup>
</script>

<template>
  <q-layout>
    <q-header
      elevated
      style="background: var(--airBlue); height: 10vh; display: flex"
    >
      <q-toolbar>
        <q-btn flat dense round icon="home" to="/" style="padding-left: 5px;"/>
        <q-toolbar-title style="padding-left: 40px; text-align: left">
          WellBookUofC
        </q-toolbar-title>

        <q-space />

        <div style="padding-right: 20px">
          <router-link v-if="sharedState.isUserLoggedIn" to="/user" class="avatar-link">
            <q-avatar icon="account_circle" size="70px"></q-avatar>
          </router-link>
        </div>
      </q-toolbar>
    </q-header>

    <div style="padding-top: 10vh">
      <router-view />
    </div>

    <q-footer elevated
    style="background: var(--salmonPink); height: 6vh; display: flex">
        <q-toolbar>
          <p style="display: inline-block; margin-left: 40%" class="q-my-auto">
            &copy; 2023 The Application. All rights reserved.
          </p>
          <q-btn class="q-mx-lg light-red-btn" label="About Us"  @click="open()" />
          <q-dialog v-model="dialog" position="bottom">
            <q-card style="width: 350px; background: #a2d0d3">
              <q-card-section class="row items-center no-wrap">
                <div>
                  <div
                    class="text-weight-bold"
                    style="margin: 10px 0; font-size: large"
                  >
                    Group7:
                  </div>
                  <ls class="text-black">
                    <li style="padding-left: 20px">Zahra Arabi</li>
                    <li style="padding-left: 20px">Mahboobeh</li>
                    <li style="padding-left: 20px">Sara</li>
                    <li style="padding-left: 20px">ah</li>
                  </ls>
                </div>
              </q-card-section>
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
      isUserLoggedIn: localStorage.getItem('isUserLoggedIn') ? localStorage.getItem('isUserLoggedIn') : false
    });

    provide('sharedState', sharedState);
    console.log(localStorage.getItem('isUserLoggedIn'))

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
      }
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
