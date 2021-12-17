<template>
  <Header />
  <div class="table-container">
    <!-- <h1 class="heading">Details of Pdf File</h1> -->
    <table class="table-list" border="1">
      <tr class="header">
        <td>Sl No.</td>
        <td>XML Name</td>
        <td>XML File</td>
        <!-- <td>Title</td>
        <td>Division</td>-->
      </tr>
      <tr class="header-list" v-for="item in datas" :key="item">
        <td>{{ item.id }}</td>
        <!-- <td>{{ item.xml_name}}</td> -->
        <td>
          <a v-on:click="xmlupload" href="#">{{ item.xml_name}}</a>
        </td>
        <!-- <td>{{ item.xml_file}}</td> -->
        <!-- <td>{{ item.read_name }}</td>
        <td>{{ item.read_title }}</td>
        <td>{{ item.read_div }}</td>-->
        <!-- <td>{{ item.read_xml }}</td> -->
        <td>
          <a :href="item.xml_file" download>
            <Button class="button">Download</Button>
          </a>
        </td>
      </tr>
    </table>
    <!-- <div>
      <button class="buttons" @click="goToPreviousPage()" v-if="showPreviousButton">Previous</button>
      <button class="buttons" @click="goToNextPage()" v-if="showNextButton">Next</button>
    </div>-->
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
      datas: [],
      showNextButton: false,
      showPreviousButton: false,
      currentPage: 1,
    };
  },
  mounted() {
    this.getData();
  },
  methods: {
    xmlupload() {
      this.$router.push({ name: "XmlListDetails" });
    },
    // goToNextPage() {
    //   this.currentPage += 1;
    //   this.getData();
    // },
    // goToPreviousPage() {
    //   this.currentPage -= 1;
    //   this.getData();
    // },
    async getData() {
      await axios
        .get("http://127.0.0.1:8000/api/xmlupload/")

        // .get(`http://127.0.0.1:8000/api/xmlupload/?page=${this.currentPage}`)
        .then((res) => {
          console.log(res.data);
          this.datas = res.data;
          // this.datas = res.data.results;
          console.log(this.info);

          // if (res.data.next) {
          //   this.showNextButton = true;
          // }

          // if (res.data.previous) {
          //   this.showPreviousButton = true;
          // }
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
  border-collapse: collapse;
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