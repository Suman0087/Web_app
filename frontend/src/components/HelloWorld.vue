<template>
  <h1>Details of Pdf File</h1>
  <div class="table-list">
    <table border="1">
      <tr>
        <td>Sl No.</td>
        <td>Name</td>
        <td>Is Password Protected</td>
        <td>Page No.</td>
        <td>Document</td>
      </tr>
      <tr v-for="item in info" :key="item">
        <td>{{ item.id }}</td>
        <td>{{ item.name }}</td>
        <td>{{ item.is_password_protected }}</td>
        <td>{{ item.page_count }}</td>
        <td>
          <!-- <a :href="item.document">{{ item.document }}</a> -->
          <a :href="item.document" download>
            <Button>
              <i class="fas fa-download" />
              Download File
            </Button>
          </a>
        </td>
      </tr>
    </table>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      info: [],
    };
  },

  async mounted() {
    const result = await axios.get("http://127.0.0.1:8000/api/upload/");
    console.log(result);
    this.info = result.data;
  },
};
</script>

<style scoped>
td {
  width: 160px;
  height: 40px;
}
table {
  border-color: black;
  border-collapse: collapse;
  color: black;
}
.table-list {
  max-width: 500px;
  margin: 50px auto;
  padding: 30px 20px;
}
</style>