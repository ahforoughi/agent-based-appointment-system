<template>
  <q-layout>
    <q-page-container class="flex flex-center" style="padding: 2rem 0">
      <q-card class="my-card" style="width: 90vw; margin-bottom: 15px">
        <q-card-section
          class="text-white"
          style="background-color: var(--airBlue)"
        >
          <div class="text-h6 belkeryBlueColor text-weight-bold">
            Your Profile
          </div>
        </q-card-section>

        <q-card-section
          class="card-container"
          style="background-color: var(--blueHoneyDoo)"
        >
          <div class="q-mb-md" style="flex: 6">
            <q-avatar size="12rem" class="q-mb-md">
              <img src="@/assets/user.jpeg" alt="avatar" />
            </q-avatar>
            <div class="text-h6">{{ userInfo.firstname }}</div>
          </div>

          <div style="flex: 6; height: 200px">
            <q-list>
              <q-item>
                <q-item-section>
                  <div class="list-item">
                    <span class="item-title">Full Name:</span>
                    <span class="item-info">{{ userInfo.fullname }}</span>
                  </div>
                </q-item-section>
              </q-item>
              <q-separator inset size="4px" class="separator" />
              <q-item>
                <q-item-section>
                  <div class="list-item">
                    <span class="item-title">UCalgary Email:</span>
                    <span class="item-info">{{ userInfo.username }}</span>
                  </div>
                </q-item-section>
              </q-item>
              <q-separator inset size="4px" class="separator" />
              <q-item>
                <q-item-section>
                  <div class="list-item">
                    <span class="item-title">Phone Number:</span>
                    <span class="item-info">{{ userInfo.phone }}</span>
                  </div>
                </q-item-section>
              </q-item>
              <!-- <q-separator inset size="4px" class="separator" />
              <q-item>
                <q-item-section>
                  <div class="list-item">
                    <span class="item-title">Address:</span>
                    <span class="item-info">{{ userInfo.username }}</span>
                  </div>
                </q-item-section>
              </q-item> -->
            </q-list>
          </div>
        </q-card-section>
      </q-card>

      <div class="row justify-around q-my-lg" style="min-width: 90%">
        <div>
          <q-btn
            label="Reseve New Time"
            class="green-btn btn-size"
            icon="event"
            @click="goToScheduler"
          />
        </div>
        <div>
          <q-btn
            flat
            label="Logout"
            icon="logout"
            @click="onLogout"
            class="light-red-btn q-py-auto btn-size"
          />
        </div>
      </div>

      <q-card
        class="reservation-card my-card"
        style="background: var(--blueHoneyDoo); margin-top: 15px"
      >
        <q-img src="@/assets/reservations.jpg" :ratio="10 / 1" />

        <q-card-section>
          <div class="text-h5 q-mt-sm text-weight-bold">
            Your Following Appointments
          </div>
        </q-card-section>

        <q-card-actions class="q-my-none">
          <q-space />
          <q-btn
            color="white"
            round
            flat
            dense
            :icon="expanded ? 'keyboard_arrow_up' : 'keyboard_arrow_down'"
            @click="expanded = !expanded"
            style="background-color: var(--asparagous)"
            :disabled="loading"
          />
        </q-card-actions>

        <q-slide-transition>
          <div v-show="expanded">
            <q-separator />
            <div v-if="doctors.length === 0" class="flex flex-center q-pa-md">
              <div class="q-mr-sm">No Reservations Found.</div>
              <q-avatar size="2em">
                <img src="@/assets/sad.png" alt="avatar" />
              </q-avatar>
            </div>
            <div
              v-else
              v-for="doctor in doctors"
              :key="doctor.appointment_id"
              class="row-container q-mb-md"
            >
              <div class="column">
                <q-item-label header>Reserved Time</q-item-label>
              </div>
              <div class="column" style="align-items: flex-start">
                <div>
                  <span class="text-weight-bold">Healthcare Provider:</span>
                  {{ doctor.doctor_name }}
                </div>
                <div>
                  <span class="text-weight-bold">Appointment Type:</span>
                  {{ doctor.doctor_specilization }}
                </div>
              </div>
              <div class="column" style="align-items: flex-start">
                <div>
                  <span class="text-weight-bold">Date:</span> {{ doctor.date }}
                </div>
                <div>
                  <span class="text-weight-bold">Time:</span> {{ doctor.time }}
                </div>
              </div>
            </div>
          </div>
        </q-slide-transition>
      </q-card>
    </q-page-container>
  </q-layout>
</template>

<script>
import { ref, inject, onMounted  } from "vue";
import { useRouter } from "vue-router";
import axios from "axios";
import { format } from "date-fns";

export default {
  setup() {
    const router = useRouter();
    const showPopup = ref(false);
    const selectedOption = ref("");
    const sharedState = inject("sharedState");
    const expanded = ref(false);
    const loading = ref(false);

    const userInfo = ref({
      firstname: localStorage.getItem("firstname"),
      fullname: localStorage.getItem("firstname") + " " + localStorage.getItem("lastname"),
      username: localStorage.getItem("username"),
      phone: localStorage.getItem("phone"),
    });

    const onLogout = () => {
      sharedState.isUserLoggedIn = false;
      sharedState.username = null;
      sharedState.firstname = null;
      sharedState.lastname = null;
      sharedState.phone = null;
      localStorage.removeItem("isUserLoggedIn");
      localStorage.removeItem("username");
      localStorage.removeItem("firstname");
      localStorage.removeItem("lastname");
      localStorage.removeItem("phone");
      router.replace("/login");
    };

    const doctors = ref([]);
    // [
    //   { appointment_id: 1, doctor_name: "Doctor1", doctor_specilization: "Therapy", date: "Monday", time: "11-12" },
    // ]

    function onItemClick(option) {
      console.log(option);
      selectedOption.value = option.label;
    }

    function goToScheduler() {
      router.push("/schedule");
    }

    async function getAppointments() {
      console.log("getAppointments");
      try {
        loading.value=true;
        const response = await axios.post(
          "http://localhost:8000/get-appointments-user",
          {
            username: localStorage.getItem("username"),
          },
          {
            headers: {
              "Content-Type": "application/json",
            },
          }
        );
        console.log("json file", typeof(response.data));
        doctors.value = response.data.map(doctor => ({
          ...doctor,
          date: format(new Date(doctor.date), "yyyy/MM/dd"),
          time: format(new Date(`1970-01-01T${doctor.time}`), "HH:mm a")
        }));
      } catch (error) {
        console.error("There was an error!", error);
      } finally {
        loading.value=false;
      }

    };

    onMounted(getAppointments);

    return {
      userInfo,
      onLogout,
      doctors,
      showPopup,
      selectedOption,
      onItemClick,
      goToScheduler,
      expanded,
      loading
    };
  },
};
</script>

<style scoped>
.my-card {
  border-radius: 10px;
}

.bg-primary {
  background: #027be3;
}

q-card-section:first-child {
  position: relative;
  overflow: hidden;
}

q-avatar img {
  border: 3px solid white;
}

.card-container {
  display: flex;
  min-height: 150px;
  align-items: center;
}

.list-item {
  margin-left: 10px;
  text-align: left;
  margin-top: 3px;
  margin-bottom: 3px;
}
.item-title {
  font-weight: bold;
}
.item-info {
  margin-left: 10px;
}
.separator {
  width: 50%;
  background: var(--asparagous);
  border-radius: 50%;
}
.btn-size {
  width: 240px;
}
.reservation-card {
  width: 90vw;
}
.row-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin: 40px 0;
}

.column {
  flex: 1;
  padding: 0 10px;
}
</style>
