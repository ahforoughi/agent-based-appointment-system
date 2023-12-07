<template>
  <q-layout>
    <q-page-container
      class="flex flex-center"
      style="padding: 2rem 0"
    >
      <q-card class="my-card" style="width: 90vw; margin-bottom: 15px;">
        <q-card-section class="bg-primary text-white">
          <div class="text-h6">User Profile</div>
        </q-card-section>

        <q-card-section class="card-container">
          <div class="q-mb-md" style="flex: 3">
            <q-avatar size="70px" class="q-mb-md">
              <img src="@/assets/user.png" alt="avatar" />
            </q-avatar>
            <div class="text-h6">{{ userInfo.name }}</div>
          </div>

          <div style="flex: 9; height: 150px'">
            <q-list bordered separator>
              <q-item>
                <q-item-section
                  class="list-item"
                  style="flex: 1 1 50%; text-align: left; font-weight: bolder"
                  >Username:</q-item-section
                >
                <q-item-section
                  class="list-item"
                  style="flex: 1 1 50%; text-align: left"
                  >{{ userInfo.username }}</q-item-section
                >
              </q-item>
              <q-separator spaced inset />
              <q-item>
                <q-item-section
                  class="list-item"
                  style="flex: 1 1 50%; text-align: left; font-weight: bolder"
                  >Email:</q-item-section
                >
                <q-item-section
                  class="list-item"
                  style="flex: 1 1 50%; text-align: left"
                  >{{ userInfo.email }}</q-item-section
                >
              </q-item>
              <q-separator spaced inset />
              <q-item>
                <q-item-section
                  class="list-item"
                  style="flex: 1 1 50%; text-align: left; font-weight: bolder"
                  >Phone Number:</q-item-section
                >
                <q-item-section
                  class="list-item"
                  style="flex: 1 1 50%; text-align: left"
                  >{{ userInfo.phone }}</q-item-section
                >
              </q-item>
            </q-list>
          </div>
        </q-card-section>

        <q-card-section>
          <q-btn
            flat
            label="Logout"
            icon="logout"
            @click="onLogout"
            class="q-ml-md"
            color="negative"
          />
        </q-card-section>
      </q-card>

      <div>
        <q-btn
          label="Reseve New Time"
          class="q-my-md"
          color="secondary"
          @click="goToScheduler"
        />
      </div>

      <div
        style="
          width: 90vw;
          margin: 20px 0;
          border: 4px solid gray;
          border-radius: 5px;
          box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.2);
          padding-bottom: 20px;
        "
      >
        <q-item-label
          header
          style="
            margin-bottom: 10px;
            font-weight: bolder;
            text-decoration: underline;
            font-size: 1.5em;
          "
        >
          List of All Doctors and Reservations
        </q-item-label>

        <div v-for="doctor in doctors" :key="doctor.id">
          <q-item tag="label" v-ripple>
            <q-item-section>
              <q-item-label>{{ doctor.name }}</q-item-label>
              <q-item-label caption>
                {{ doctor.info }}
              </q-item-label>
            </q-item-section>
          </q-item>
        </div>
      </div>
    </q-page-container>
  </q-layout>
</template>

<script>
import { ref } from "vue";
import { useRouter } from "vue-router";
import { Notify } from "quasar";

export default {
  setup() {
    const router = useRouter();
    const showPopup = ref(false);
    const selectedOption = ref("");

    const userInfo = ref({
      name: "zahra",
      username: "name",
      email: "test@",
      phone: "2222",
    });

    const onLogout = () => {
      router.replace("/login");
    };

    const doctors = ref([
      { id: 1, name: "Doctor1", info: "The info for Doctor1" },
      { id: 2, name: "Doctor2", info: "The info for Doctor2" },
      { id: 3, name: "Doctor3", info: "The info for Doctor3" },
    ]);

    function onItemClick(option) {
      console.log(option);
      selectedOption.value = option.label;
    }

    function goToScheduler() {
      router.push("/schedule");
    }

    return {
      userInfo,
      onLogout,
      doctors,
      showPopup,
      selectedOption,
      onItemClick,
      goToScheduler,
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
  margin: 5px 0;
}
</style>
