<template>
	<div class="container">
		<div>
			<h2>Upload File</h2>
			<hr/>
        
            <label>Title
                <input type="text" v-model="form.first_name"/>
            </label>
            <label>Description
                <input type="text" v-model="form.first_name"/>
            </label>
        
			<label>File
				<input type="file" @change="handleFileUpload( $event )"/>
			</label>
			<br>
			<button v-on:click="submitFile()">Submit</button>
		</div>
	</div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
