<template>
<div>
  <el-form :model="form" status-icon ref="form" label-width="100px"
    class="demo-ruleForm">
    <el-form-item label="Address" prop="addr"
      :rules="[
        { required: true, message: 'Address is required'}
      ]"
    >
      <el-input v-model="form.addr" auto-complete="off"></el-input>
    </el-form-item>
    <el-form-item label="Size (sqf)" prop="size"
      :rules="[
        { required: true, message: 'Size is required'},
        { type: 'number', message: 'Size must be a number'}
      ]"
    >
      <el-input v-model="form.size"></el-input>
    </el-form-item>
    <el-form-item label="Level" prop="lvl"
      :rules="[
        { type: 'number', message: 'Level must be a number'}
      ]"
    >
      <el-input v-model="form.lvl"></el-input>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="submitForm('form')">Submit</el-button>
      <el-button @click="resetForm('form')">Reset</el-button>
    </el-form-item>
  </el-form>
</div>
</template>

<script>
export default {
  name: 'ComponentUserInput',
  data() {
    return {
      form: {
        addr: '',
        size: '',
        lvl: '',
      },
    };
  },
  methods: {
    submitForm(formName) {
      console.log(this.$refs[formName]);
    },
    resetForm(formName) {
      this.$refs[formName].resetFields();
    },
  },
};
</script>

<style scoped>
</style>
