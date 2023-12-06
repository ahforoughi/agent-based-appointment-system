<script setup>
</script>

<template>
  <q-layout>
    <q-header
      elevated
      style="background: rgb(87 107 164); height: 10vh; display: flex"
    >
      <q-toolbar>
        <q-btn flat dense round icon="menu" to="/" />
        <q-toolbar-title style="padding-left: 40px; text-align: left">
          Application Name
        </q-toolbar-title>

        <q-space />

        <div style="padding-right: 20px">
          <router-link v-if="isUserLoggedIn" to="/user" class="avatar-link">
            <q-avatar icon="account_circle" size="70px"></q-avatar>
          </router-link>
        </div>
      </q-toolbar>
    </q-header>

    <div style="padding-top: 10vh">
      <router-view />
    </div>

    <div class="footer">
      <p style="display: inline-block; margin-right: 20px">
        &copy; 2023 The Application. All rights reserved.
      </p>
      <q-btn label="About Us" color="secondary" @click="open()" />
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
    </div>
  </q-layout>
</template>

<script>
import { ref } from "vue";

export default {
  setup() {
    const dialog = ref(false);
    const position = ref("bottom");
    const isUserLoggedIn = ref(true);

    return {
      dialog,
      position,
      isUserLoggedIn,

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
