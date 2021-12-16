 <template>
  <Header />
  <div class="card">
    <div class="container">
      <div class="form-control">
        <h2 class="heads">Upload XML File</h2>
        <label>
          Name
          <input type="text" v-model="xml_name" />
        </label>
        <br />
        <br />
        <label>
          Upload XML File
          <input type="file" @change="handleFileUpload($event)" />
        </label>
        <br />
        <br />
      </div>
      <button class="submit-button" v-on:click="submitFile()">Submit</button>
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
      xml_name: "",
      xml_file: "",
    };
  },
  methods: {
    handleFileUpload(event) {
      this.xml_file = event.target.files[0];
    },
    submitFile() {
      let formData = new FormData();
      formData.append("xml_name", this.xml_name);
      formData.append("xml_file", this.xml_file);

      axios
        .post("http://127.0.0.1:8000/api/xmlupload/", formData)
        .then(function (res) {
          console.log(res);
        });
    },
  },
};
</script>

<style>
.card {
  display: flex;
}
.container {
  background-color: #b4b4b462;
  max-width: 300px;
  margin: 40px auto;
  margin-top: 5rem;
  padding: 30px 20px;
  box-shadow: 2px 5px 10px rgba(0, 0, 0, 0.5);
}
.heads {
  text-align: center;
}
.form-control {
  text-align: left;
  margin-bottom: 25px;
}
.form-control input,
.form-control select,
.form-control textarea {
  border: 1px solid #777;
  border-radius: 4px;
  padding: 10px;
  width: 90%;
}
.submit-button {
  background-color: #16a085;
  border-radius: 5px;
  width: 80px;
  font-size: 20px;
  text-align: center;
}
</style>
