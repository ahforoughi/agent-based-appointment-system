<template>
  <div class="q-pa-md">
    <h6
      style="
        padding: 20px 40px;
        border: 1px solid #e0e0e0;
        width: max-content;
        margin: 40px auto;
        background: #c4edfa;
        border-radius: 10px;
      "
    >
      You can select your appropriate appointment.
    </h6>
    <q-table
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
    <div class="row justify-center q-mt-md">
      <q-btn
        label="Add to the appointments"
        color="green"
        @click="addAppointment"
        :disabled="selected.length == 0"
      />
    </div>
  </div>
</template>

<script>
import { ref, computed, nextTick, toRaw } from "vue";
import { Notify } from "quasar";

const columns = [
  {
    name: "doctor",
    required: true,
    label: "Doctor Name",
    align: "left",
    field: (row) => row.name,
    format: (val) => `${val}`,
    sortable: true,
  },
  {
    name: "day",
    required: true,
    align: "center",
    label: "Day",
    field: "day",
    sortable: true,
  },
];

const rows = [
  {
    id: 1,
    name: "Frozen Yogurt",
    day: 159,
  },
  {
    id: 2,
    name: "Ice cream sandwich",
    day: 237,
  },
  {
    id: 3,
    name: "Eclair",
    day: 262,
  },
  {
    id: 4,
    name: "Cupcake",
    day: 305,
  },
  {
    id: 5,
    name: "Gingerbread",
    day: 356,
  },
  {
    id: 6,
    name: "Jelly bean",
    day: 375,
  },
  {
    id: 7,
    name: "Lollipop",
    day: 392,
  },
  {
    id: 8,
    name: "Honeycomb",
    day: 408,
  },
  {
    id: 9,
    name: "Donut",
    day: 452,
  },
  {
    id: 10,
    name: "KitKat",
    day: 518,
  },
];

export default {
  setup() {
    const tableRef = ref(null);

    const navigationActive = ref(false);
    const pagination = ref({});
    const selected = ref([]);

    const filter = ref("");

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
      addAppointment
    };
  },
};
</script>
