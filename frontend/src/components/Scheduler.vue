<template>
  <div class="q-pa-md q-mx-md">
    <div class="row justify-between q-mx-lg">
      <h4 class="text-left q-pt-lg belkeryBlueColor">Appointment Scheduler</h4>
      <div class="q-py-auto q-my-auto row justify-between">
        <div class="q-pa-md" style="min-width: 300px">
          <div class="q-gutter-md">
            <q-select
              rounded
              outlined
              v-model="selected_appointment_type"
              :options="options"
              label=" Appointment Type"
              input-class="custom-select-input"
              option-class="custom-option"
            />
          </div>
        </div>
        <div class="q-my-auto q-ml-md">
          <q-btn
            class="blue-btn"
            padding="xs lg"
            label="Search"
            @click="SearchType"
          />
        </div>
      </div>
    </div>
    <div class="row justify-end q-my-md q-mr-xl">
      <q-btn
        label="Add to the appointments"
        class="green-btn"
        @click="addAppointment"
        :disabled="isButtonDiabled"
      />
    </div>
    <q-table
      class="q-mx-lg"
      style="background-color: var(--chamRed)"
      flat
      bordered
      ref="tableRef"
      :class="tableClass"
      tabindex="0"
      title="Available Appointments"
      :rows="rows"
      :columns="columns"
      row-key="appointment_id"
      selection="single"
      v-model:selected="selected"
      :pagination="pagination"
      :filter="filter"
      @focusin="activateNavigation"
      @focusout="deactivateNavigation"
      @keydown="onKey"
      :loading="loading"
    >
      <template v-slot:top-right>
        <q-input
          borderless
          dense
          debounce="300"
          v-model="filter"
          placeholder="Search"
        >
          <template v-slot:append>
            <q-icon name="search" />
          </template>
        </q-input>
      </template>
    </q-table>
  </div>
</template>

<script>
import { ref, computed, nextTick, toRaw, watch, onMounted } from "vue";
import { Notify } from "quasar";
import { useRouter } from "vue-router";
import { format } from "date-fns";
import axios from "axios";

export default {
  setup() {
    const tableRef = ref(null);
    const navigationActive = ref(false);
    const pagination = ref({});
    const router = useRouter();
    const selected = ref([]);
    const options = ref([
      "Medical",
      "Mental Health",
      "Chiropractic",
      "Massage",
    ]);
    const selected_appointment_type = ref("all");
    const filter = ref("");
    const loading = ref(false);

    const columns = ref([
      {
        name: "doctor",
        required: true,
        label: "Health Care Provider Name",
        align: "left",
        field: (row) => row.doctor_name,
        format: (val) => `${val}`,
        sortable: true,
      },
      {
        name: "doctor_specilization",
        required: true,
        label: "Health Care Provider Specilization",
        align: "left",
        field: (row) => row.doctor_specilization,
        format: (val) => `${val}`,
        sortable: true,
      },
      {
        name: "date",
        required: true,
        align: "center",
        label: "Date",
        field: (row) => row.date,
        format: (val) => format(new Date(val), "yyyy/MM/dd"),
        sortable: true,
      },
      {
        name: "time",
        required: true,
        align: "center",
        label: "Time",
        field: (row) => row.time,
        format: (val) => format(new Date(`1970-01-01T${val}`), "HH:mm a"),
        sortable: true,
      },
    ]);

    const rows = ref([
      // {
      //   appointment_id: 1,
      //   doctor_specilization: "medical",
      //   doctor_name: "Iona",
      //   time: "11:00:00",
      //   date: "2023-12-13T00:00:00",
      // },
    ]);

    function onKey(evt) {
      if (
        navigationActive.value !== true ||
        [33, 34, 35, 36, 38, 40].indexOf(evt.keyCode) === -1 ||
        tableRef.value === null
      ) {
        return;
      }

      evt.preventDefault();

      const { computedRowsNumber, computedRows } = tableRef.value;

      if (computedRows.length === 0) {
        return;
      }

      const currentIndex =
        selected.value.length > 0
          ? computedRows.indexOf(toRaw(selected.value[0]))
          : -1;
      const currentPage = pagination.value.page;
      const rowsPerPage =
        pagination.value.rowsPerPage === 0
          ? computedRowsNumber
          : pagination.value.rowsPerPage;
      const lastIndex = computedRows.length - 1;
      const lastPage = Math.ceil(computedRowsNumber / rowsPerPage);

      let index = currentIndex;
      let page = currentPage;

      switch (evt.keyCode) {
        case 36: // Home
          page = 1;
          index = 0;
          break;
        case 35: // End
          page = lastPage;
          index = rowsPerPage - 1;
          break;
        case 33: // PageUp
          page = currentPage <= 1 ? lastPage : currentPage - 1;
          if (index < 0) {
            index = 0;
          }
          break;
        case 34: // PageDown
          page = currentPage >= lastPage ? 1 : currentPage + 1;
          if (index < 0) {
            index = rowsPerPage - 1;
          }
          break;
        case 38: // ArrowUp
          if (currentIndex <= 0) {
            page = currentPage <= 1 ? lastPage : currentPage - 1;
            index = rowsPerPage - 1;
          } else {
            index = currentIndex - 1;
          }
          break;
        case 40: // ArrowDown
          if (currentIndex >= lastIndex) {
            page = currentPage >= lastPage ? 1 : currentPage + 1;
            index = 0;
          } else {
            index = currentIndex + 1;
          }
          break;
      }

      if (page !== pagination.value.page) {
        pagination.value.page = page;

        nextTick(() => {
          const { computedRows } = tableRef.value;
          selected.value = [
            computedRows[Math.min(index, computedRows.length - 1)],
          ];
          tableRef.value.$el.focus();
        });
      } else {
        selected.value = [computedRows[index]];
      }
    }

    async function SearchType() {
      var appoinment_type = "all";
      if (selected_appointment_type.value) {
        if (selected_appointment_type.value == "Medical") {
          appoinment_type = "medical";
        } else if (selected_appointment_type.value == "Mental Health") {
          appoinment_type = "mental_health";
        } else if (selected_appointment_type.value == "Chiropractic") {
          appoinment_type = "chiropractic";
        } else if (selected_appointment_type.value == "Massage") {
          appoinment_type = "massage";
        }
        console.log("correct", selected_appointment_type.value);
      }
      try {
        loading.value = true;
        const response = await axios.post(
          "http://localhost:8000/appointments",
          {
            appoinment_type: appoinment_type,
          },
          {
            headers: {
              "Content-Type": "application/json",
            },
          }
        );
        console.log("json file", response.data);
        rows.value = response.data;
        console.log("rows value", rows.value);
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

    function sendEmail() {
      try {
        const response = axios.post("http://localhost:8000/send-email", {
          username: localStorage.getItem("username"),
        });
        console.log("email sent:", response.data);
      } catch (error) {
        console.error("There was an error with sending email!", error);
      }
    }

    function sendReminder() {
      try {
        const response = axios.post("http://localhost:8000/send-reminder", {
          username: localStorage.getItem("username"),
          date: selected.value[0].date
        });
        console.log("email reminder sent:", response.data);
      } catch (error) {
        console.error("There was an error with sending email!", error);
      }
    }

    async function addAppointment() {
      console.log(selected.value[0].appointment_id);
      var id = selected.value[0].appointment_id;
      try {
        loading.value = true;
        const response = await axios.post(
          "http://localhost:8000/set-appointments",
          {
            appointment_id: id,
            username: localStorage.getItem("username"),
          }
        );
        console.log(response.data);
        Notify.create({
          color: "green-5",
          message: "Reservation was successful!",
          icon: "check",
          position: "center",
          classes: "q-py-md q-px-lg",
        });
        sendEmail();
        sendReminder();
        router.replace("/user");
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

    const isButtonDiabled = computed(() => {
      if (selected.value.length === 0) {
        return true;
      }
      return loading.value;
    });

    onMounted(SearchType);

    return {
      tableClass: computed(() =>
        navigationActive.value === true ? "shadow-8 no-outline" : null
      ),

      activateNavigation() {
        navigationActive.value = true;
      },

      deactivateNavigation() {
        navigationActive.value = false;
      },

      tableRef,
      navigationActive,
      filter,
      selected,
      pagination,
      columns,
      rows,
      onKey,
      addAppointment,
      options,
      columns,
      selected_appointment_type,
      SearchType,
      loading,
      isButtonDiabled,
    };
  },
};
</script>

<style scoped></style>
