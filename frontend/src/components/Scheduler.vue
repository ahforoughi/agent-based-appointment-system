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
          <q-btn class="blue-btn" padding="xs lg" label="Search" />
        </div>
      </div>
    </div>
    <div class="row justify-end q-my-md q-mr-xl">
      <q-btn
        label="Add to the appointments"
        class="green-btn"
        @click="addAppointment"
        :disabled="selected.length == 0"
      />
    </div>
    <q-table
      class="q-mx-lg"
      flat
      bordered
      ref="tableRef"
      :class="tableClass"
      tabindex="0"
      title="Available Appointments"
      :rows="rows"
      :columns="columns"
      row-key="name"
      selection="single"
      v-model:selected="selected"
      :pagination="pagination"
      :filter="filter"
      @focusin="activateNavigation"
      @focusout="deactivateNavigation"
      @keydown="onKey"
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
import { ref, computed, nextTick, toRaw } from "vue";
import { Notify } from "quasar";
import { useRouter } from "vue-router";
import { format } from 'date-fns';

export default {
  setup() {
    const tableRef = ref(null);
    const navigationActive = ref(false);
    const pagination = ref({});
    const router = useRouter();
    const selected = ref([]);
    const options = ref([
      "Medical",
      "Therapy",
      "Chiropractic",
      "Physiotherapy"
    ]);
    const selected_appointment_type = ref(null);
    const filter = ref("");

    const columns = ref([
      {
        name: "doctor",
        required: true,
        label: "Health Care Provider Name",
        align: "left",
        field: (row) => row.name,
        format: (val) => `${val}`,
        sortable: true,
      },
      {
        name: "type",
        required: true,
        label: "Type",
        align: "left",
        field: (row) => row.type,
        format: (val) => `${val}`,
        sortable: true,
      },
      {
        name: "Date",
        required: true,
        align: "center",
        label: "Date",
        field: (row) => row.date,
        format: (val) => format(new Date(val), 'yyyy/MM/dd'),
        sortable: true,
      },
      {
        name: "Time",
        required: true,
        align: "center",
        label: "Time",
        field: (row) => row.time,
        format: (val) => format(new Date(`1970-01-01T${val}`), 'HH:mm a'),
        sortable: true,
      },
    ]);

    const rows = ref([
      {
        id: 1,
        name: "Frozen Yogurt",
        date: "1998-05-15",
        time: "14:30:00",
        type: "Physiotherapy",
      },
      {
        id: 2,
        name: "Ice cream sandwich",
        date: "1990-05-15",
        time: "16:30:00",
        type: "Chiropractic",
      },
      {
        id: 3,
        name: "Eclair",
        date: "1993-05-15",
        time: "12:30:00",
        type: "Therapy",
      },
      {
        id: 4,
        name: "Cupcake",
        date: "1990-05-15",
        time: "12:30:00",
        type: "Chiropractic",
      },
      {
        id: 5,
        name: "Gingerbread",
        date: "1990-05-15",
        time: "10:50:00",
        type: "Medical",
      },
      {
        id: 6,
        name: "Jelly bean",
        date: "1990-05-15",
        time: "14:30:00",
        type: "Chiropractic",
      },
      {
        id: 7,
        name: "Lollipop",
        date: "1990-05-15",
        time: "19:30:00",
        type: "Medical",
      },
      {
        id: 8,
        name: "Honeycomb",
        date: "1990-05-15",
        time: "10:30:00",
        type: "Physiotherapy",
      },
      {
        id: 9,
        name: "Donut",
        date: "1990-05-15",
        time: "15:30:00",
        type: "Therapy",
      },
      {
        id: 10,
        name: "KitKat",
        date: "1990-05-15",
        time: "14:30:00",
        type: "Medical",
      },
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

    function addAppointment() {
      console.log(selected.value[0].id);
      // server and redirect to the user
      if (selected.value[0].id) {
        
        Notify.create({
          color: "positive",
          message: "successful",
          icon: "check",
          position: "center",
        });
        router.replace("/user");
        
      } else {
        Notify.create({
          color: "negative",
          message: "not successful",
          icon: "error",
          position: "center",
        });
      }
    }

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
      selected_appointment_type
    };
  },
};
</script>

