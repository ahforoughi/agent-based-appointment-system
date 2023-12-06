<template>
  <q-layout style="min-height: 80vh">
    <q-page-container class="flex flex-center q-page-class">
      <div class="text-center">
        <div class="q-mb-md">
          <q-avatar size="10rem">
            <img src="@/assets/vue.svg" alt="logo" />
          </q-avatar>
        </div>
        <div class="text-h5 q-my-md">Welcome to our Application.</div>
        <q-btn label="Login" to="/login" class="q-mr-md" color="primary" />
        <q-btn label="Register" to="/register" color="secondary" />
      </div>
    </q-page-container>
  </q-layout>
</template>

<script>
export default {
  name: "LandingPage",
};
</script>

<style>
.q-page-class {
  height: 400px;
}
</style>