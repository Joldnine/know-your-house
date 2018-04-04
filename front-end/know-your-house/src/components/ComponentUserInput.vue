<template>
  <div>
    <el-form :model="form" ref="form" label-width="100px"
      class="demo-ruleForm">
      <el-row>
        <el-col :xs="24" :sm="24" :md="24" :lg="24" :xl="24">
          <el-form-item label="Street" prop="street"
            :rules="[
              { required: true, message: 'Street is required'}
            ]">
            <el-input v-model="form.street" auto-complete="off"></el-input>
          </el-form-item>
        </el-col>
        <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12">
          <el-form-item label="Block" prop="block"
            :rules="[
              { required: true, message: 'Block is required'}
            ]">
            <el-input v-model="form.block" auto-complete="off"></el-input>
          </el-form-item>
        </el-col>
        <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12">
          <el-form-item label="Flat type" prop="flatType"
            :rules="[
              { required: true, message: 'Flat type is required'}
            ]">
            <el-select v-model="form.flatType" placeholde="Select" style="width:100%;">
              <el-option
                v-for="item in flatTypeOpts"
                :key="item.value"
                :label="item.label"
                :value="item.value">
              </el-option>
            </el-select>
          </el-form-item>
        </el-col>
        <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12">
          <el-form-item label="Size (sqm)" prop="size"
            :rules="[
              { required: true, message: 'Size is required'},
              { type: 'number', message: 'Size must be a number'}
            ]">
            <el-input v-model.number="form.size"></el-input>
          </el-form-item>
        </el-col>
        <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12">
          <el-form-item label="Floor" prop="floor"
            :rules="[
              { type: 'number', message: 'Floor must be a number'}
            ]">
            <el-input-number v-model="form.floor"
              :min="1" :max="100" style="width:100%;"></el-input-number>
          </el-form-item>
        </el-col>
      </el-row>
      <el-row>
        <el-form-item>
          <el-button type="primary" @click="submitForm('form')">Submit</el-button>
          <el-button @click="resetForm('form')">Reset</el-button>
        </el-form-item>
      </el-row>
    </el-form>
  </div>
</template>

<script>
import { getGeocode, getPrediction } from '@/api';

export default {
  name: 'ComponentUserInput',
  data() {
    return {
      flatTypeOpts: [
        {
          value: '3 Room',
          label: '3 Room',
        }, {
          value: '4 Room',
          label: '4 Room',
        }, {
          value: '5 Room',
          label: '5 Room',
        },
      ],
      form: {
        street: '',
        block: '',
        flatType: '',
        size: '',
        floor: '',
      },
    };
  },
  computed: {
    predictionForm: {
      get() {
        const townArea = this.$store.getters.getTown.toUpperCase();
        const flatType = this.form.flatType.toUpperCase();
        const areaSqm = parseInt(this.form.size, 10);
        const age = (new Date()).getFullYear() - parseInt(this.$store.getters.getHouseAge, 10);
        const floor = parseInt(this.form.floor, 10);
        const mrtDistance = this.$store.getters.getMrtDistance;
        const nearByPlaces = this.$store.getters.getNearbyPlaces;
        const numMall = nearByPlaces.filter(e => e.type === 'mall').length;
        const numMrt = nearByPlaces.filter(e => e.type === 'mrt').length;
        const numSchool = nearByPlaces.filter(e => e.type === 'school').length;
        return {
          town_area: townArea,
          flat_type: flatType,
          area_sqm: areaSqm,
          age,
          floor,
          mrt_distance: mrtDistance,
          num_mall: numMall,
          num_mrt: numMrt,
          num_school: numSchool,
        };
      },
    },
  },
  methods: {
    submitForm() {
      this.$store.commit('SET_PAGE_LOADING', true);
      this.$store.commit('SET_PAGE_CONTENT_LOADED', false);
      this.$store.commit('EDIT_USER_INPUT_ADDRESS', this.form.street);
      const street = this.form.street;
      this.$store.dispatch('requestTownByStreet', { street });
      this.$store.dispatch('requestMrtDistance', { street });
      let loc = {};
      getGeocode(this.form.street).then((result) => {
        loc = result.body;
        this.$store.commit('EDIT_USER_INPUT_ADDRESS_LOC', JSON.parse(loc));
        this.$store.dispatch('requestNearbyPlaces', { loc }).then(() => {
          const query = this.predictionForm;
          getPrediction(query).then((resultPrice) => {
            const price = parseInt(JSON.parse(resultPrice.body).price, 10);
            this.$store.commit('SET_PRICE', price);
            this.$store.commit('SET_PAGE_LOADING', false);
            this.$store.commit('SET_PAGE_CONTENT_LOADED', true);
          }).catch(() => {
            this.$store.commit('SET_PAGE_LOADING', false);
            this.$message('Failed to load data.');
          });
        }).catch(() => {
          this.$store.commit('SET_PAGE_LOADING', false);
          this.$message('Failed to load data.');
        });
      }).catch(() => {
        this.$store.commit('SET_PAGE_LOADING', false);
        this.$message('Failed to load data.');
      });
      this.$store.dispatch('requestPriceHistory',
        { street: this.form.street, block: this.form.block, flatType: this.form.flatType });
    },
    resetForm(formName) {
      this.$refs[formName].resetFields();
      this.$store.commit('RESET_USER_INPUT_ADDRESS');
      this.$store.commit('SET_PAGE_CONTENT_LOADED', false);
    },
  },
};
</script>

<style scoped>
</style>
