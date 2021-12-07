<template>
  <Header />
  <div class="table-container">
    <!-- <h1 class="heading">Details of Pdf File</h1> -->
    <table class="table-list" border="1">
      <tr class="header">
        <td>Sl No.</td>
        <td>Name</td>
        <td>Is Password Protected</td>
        <td>Page No.</td>
        <td>Document</td>
        <!-- <td>Document</td> -->
        <!-- <td>Document</td> -->
      </tr>
      <tr class="header-list" v-for="item in info" :key="item">
        <td>{{ item.id }}</td>
        <td>{{ item.name }}</td>
        <td>{{ item.is_password_protected }}</td>
        <td>{{ item.page_count }}</td>
        <!-- <td>{{ item.xml_file }}</td> -->
        <!-- <td>{{ item.read_xml }}</td> -->
        <td>
          <!-- <a :href="item.document">{{ item.document }}</a> -->
          <a :href="item.pdf_file" download>
            <Button class="button">Download</Button>
          </a>
        </td>
      </tr>
    </table>
    <div>
      <button class="buttons" @click="goToPreviousPage()" v-if="showPreviousButton">Previous</button>
      <button class="buttons" @click="goToNextPage()" v-if="showNextButton">Next</button>
    </div>
  </div>
</template>

<script>
import Header from "./Header.vue";
import axios from "axios";

export default {
  components: {
    Header,
  },
  data() {
    return {
      info: [],
      showNextButton: false,
      showPreviousButton: false,
      currentPage: 1,
    };
  },
  mounted() {
    this.getData();
  },
  methods: {
    goToNextPage() {
      this.currentPage += 1;
      this.getData();
    },
    goToPreviousPage() {
      this.currentPage -= 1;
      this.getData();
    },
    async getData() {
      await axios
        // .get("http://127.0.0.1:8000/api/upload/")

        .get(`http://127.0.0.1:8000/api/upload/?page=${this.currentPage}`)
        .then((res) => {
          console.log(res.data);
          this.info = res.data.results;
          // console.log(this.info);

          if (res.data.next) {
            this.showNextButton = true;
          }

          if (res.data.previous) {
            this.showPreviousButton = true;
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style>
.table-container {
  padding: 0 230px;
  margin-top: 0rem;
  font-size: 15px;
}
.heading {
  font-size: 35px;
  text-align: center;
  width: 100%;
  padding-left: 0px;
  background-color: #16a085;
  box-shadow: 2px 2px 12px rgba(0, 0, 0, 0.2), -1px -1px 8px rgba(0, 0, 0, 0.2);
}

td {
  width: 150px;
}

.header-list:hover {
  box-shadow: 2px 2px 12px rgba(0, 0, 0, 0.2), -1px -1px 8px rgba(0, 0, 0, 0.2);
}
.header {
  background-color: #16a085;
  color: #fff;
  font-size: 20px;
}
.table-list {
  margin-top: -2rem;
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  border-collapse: collapse;
  width: 66%;
  box-shadow: 2px 2px 12px rgba(0, 0, 0, 0.2), -1px -1px 8px rgba(0, 0, 0, 0.2);
}
.list {
  background-color: #16a085;
  margin-top: 2px;
  margin-left: 30px;
}
.button {
  background-color: #16a085;
  border-radius: 5px;
  width: 85px;
  font-size: 16px;
  text-align: center;
}
.buttons {
  margin-top: 25rem;
  background-color: #16a085;
  border-radius: 5px;
  width: 85px;
  font-size: 16px;
  text-align: center;
}
</style>