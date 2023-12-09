<template>
  <q-layout style="min-height: 70vh">
    <q-page-container class="flex flex-center q-page-class q-p-xl">
      <div class="text-center">
        <div class="q-my-md">
          <q-avatar size="15rem">
            <img src="@/assets/logo-1.1.png" alt="logo" />
          </q-avatar>
        </div>
        <div class="q-px-xl">
          <div class="text-h5 q-my-md">Welcome to Student Wellness sevices booking Website.</div>
          <!-- <div class="text-h7 q-my-md">You can book  a new appointment or see your following appointments with the University of Calgary wellness center. </div>
          <div class="text-h7 q-my-md q-mx-l q-px-xl">Experience a variety of health services tailored to your needs. We offer medical appointments, therapy sessions, chiropractic, and physiotherapy to support your well-being. 
          Our dedicated team is here to provide personalized care for a healthier you.</div> -->
          <div class="text-h7 q-my-lg q-mx-lg text-center">
            <p style="margin: 0 auto">You can book a new appointment or see your following appointments with the University of Calgary wellness center.</p>
            Experience a variety of health services tailored to your needs. We offer medical appointments, therapy sessions, chiropractic, and physiotherapy to support your well-being. 
          Our dedicated team is here to provide personalized care for a healthier you.
          </div>
          <q-btn label="Login" to="/login" class="q-mr-md green-btn btn-size" />
          <q-btn label="Register" to="/register" class="blue-btn btn-size" />
        </div>
      </div>
    </q-page-container>
  </q-layout>
</template>

<script>
</script>

<style>
.q-page-class {
  height: 400px;
}
</style>