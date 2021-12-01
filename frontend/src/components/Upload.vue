<template>
  <div class="container">
    <div class="form-control">
      <h2>Upload File</h2>
      <label>
        Name
        <input type="text" v-model="name" />
      </label>
      <br />
      <br />
      <label>
        File
        <input type="file" @change="handleFileUpload($event)" />
      </label>
      <br />

      <br />

      <button v-on:click="submitFile()">Submit</button>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      name: "",
      document: "",
    };
  },

  methods: {
    handleFileUpload(event) {
      this.document = event.target.files[0];
    },

    submitFile() {
      let formData = new FormData();

      formData.append("name", this.name);
      formData.append("document", this.document);

      axios
        .post("http://127.0.0.1:8000/api/upload/", formData)
        .then(function () {
          console.log("SUCCESS!!");
        });
    },
  },
};
</script>

<style scoped>
.container {
  max-width: 20rem;
  margin: 50px auto;
  padding: 30px 20px;
  box-shadow: 2px 5px 10px rgba(0, 0, 0, 0.5);
}
.form-control {
  text-align: left;
  margin-bottom: 25px;
}
</style>