<template>
  <section class="multi_step_form">
    <form id="msform">
      <!-- Tittle -->
      <div class="tittle">
        <h2>NFT Verification Process</h2>
        <p>In order to upload your work to NFT, we have to complete the similarity analysis process</p>
      </div>
      <!-- progressbar -->
      <ul id="progressbar">
        <li v-bind:class="{active: slide>=0}">Description</li>
        <li v-bind:class="{active: slide>=1}">Upload Image</li>
        <li v-bind:class="{active: slide>=2}">Similarity Analysis</li>
      </ul>
      <!-- fieldsets -->
      <fieldset v-if="slide===0">
        <h3>NFT details</h3>
        <h6>Let us verify NFT name and description.</h6>
        <div class="form-row">
          <div class="form-group col-md-6">
            <input type="text" v-model="form.name" class="form-control" placeholder="NFT name">
          </div>
          <div class="form-group col-md-6">
            <input type="text" v-model="form.description" class="form-control" placeholder="Description">
          </div>
        </div>
        <br><br>
        <button type="button" class="next action-button" @click="slide+=1">Continue</button>
      </fieldset>
      <fieldset v-if="slide===1">
        <h3>Image Veriftion</h3>
        <h6>Please upload your work to verify it's uniqueness.</h6>
        <div class="passport">
          <h4>PNG <br>JPG <br>JPEG.</h4>
          <a href="#" class="don_icon"><i class="ion-android-done"></i></a>
        </div>
        <div class="file-input">
          <div class="form-group">
            <input type="file" @change="onFileChange" name="file" id="file" class="input-file">
            <label for="file" class="btn btn-tertiary js-labelFile">
              <i class="icon fa fa-check"></i>
              <span class="js-fileName">Choose file</span>
            </label>
          </div>
        </div>
        <button type="button" class="action-button previous previous_button" @click="slide-=1">Back</button>
        <button type="button" class="next action-button" @click="sendFiles">Continue</button>
      </fieldset>
      <fieldset v-if="slide===2">
        <h3>Create Security Questions</h3>
        <h6>Please update your account with security questions</h6>
        <div class="form-group">
          <img v-for="(el, i) in resp.similar" :key="i" :src="el">
        </div>
        <h6>SSDEEP: {{ resp.ssdeep }}.</h6>
        <h6>Unique: {{ resp.unique*100 }}%.</h6>
        <h6>SHA1: {{ resp.sha1 }}.</h6>
        <button type="button" class="action-button previous previous_button" @click="slide-=1">Back</button>
        <a href="#" class="action-button">Finish</a>
      </fieldset>
    </form>
  </section>
</template>

<script>
import axios from 'axios'

const baseURL = 'http://137.184.112.242:5000/api'

export default {
  name: 'App',
  data() {
    return {
      slide: 0,
      form: {
        name: '',
        description: ''
      },
      resp:{
        ssdeep: '98304:nP10dW4Zul+87vA2trigm0tzd3WFb1qpLjS1mAr9hO3f+B7:nPSbElBvtlltPWIe1mlPK',
        unique: 0.99,
        sha1: '0029a46aae6b83cf2d2ecb25f72208eabcd8f4eb',
        similar:[
          'https://img.rarible.com/prod/image/upload/t_image_preview/prod-itemImages/0x49cf6f5d44e70224e2e23fdcdd2c053f30ada28b:13295/de6b48ec',
          'https://img.rarible.com/prod/image/upload/t_image_preview/prod-itemImages/0x49cf6f5d44e70224e2e23fdcdd2c053f30ada28b:4349/da2e08a',
          'https://img.rarible.com/prod/image/upload/t_image_preview/prod-itemImages/0x49cf6f5d44e70224e2e23fdcdd2c053f30ada28b:9997/317907aa',
        ]
      },
      file: null
    }
  },
  methods: {
    sendFiles() {
      const formData = new FormData()
      formData.append('file_object',this.file)
      formData.append('name', this.form.name)
      formData.append('description', this.form.description)
      this.slide+=1;
      return axios
          .post(`${baseURL}/check/`, formData,  {
            headers: { 'Content-Type': 'multipart/form-data' },
          })
          .then(r => r.data)

    },
    onFileChange(e) {
      let files = e.target.files || e.dataTransfer.files
      if (!files.length)
        return;
      this.file = files[0]
      console.log(this.file)
    },
  }
}
</script>

<style>
#app {
  font-family: 'Roboto', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;

  text-align: center;
  color: #769CF6;
  margin-top: 60px;
}

.file-input .btn-tertiary {
  color: #5f6771;
  padding: 0;
  line-height: 40px;
  width: 200px;
  margin: auto;
  margin-bottom: 5%;
  display: block;
  border: 2px solid #5f6771
}

.file-input .btn-tertiary:hover, .file-input .btn-tertiary:focus {
  color: white;
  border-color: #769CF6;
  background-color: #769CF6;
}

.fa-check{
  margin-right: 10px;
}

.file-input .input-file {
  width: .1px;
  height: .1px;
  opacity: 0;
  overflow: hidden;
  position: absolute;
  z-index: -1
}

.file-input .input-file + .js-labelFile {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  padding: 0 10px;
  cursor: pointer
}

.file-input .input-file + .js-labelFile .icon:before {
  content: "\f093"
}

.file-input .input-file + .js-labelFile.has-file .icon:before {
  content: "\f00c";
  color: #5AAC7B
}
</style>

<style lang="scss">
/*font Variables*/
$roboto: 'Roboto', sans-serif;
/*Color Variables*/
$bc: #2A64F6;
$heding: #769CF6;
$pfont: #5f6771;

// Mixins
@mixin transition($property: all, $duration: 300ms, $animate: linear, $delay:0s) {
  transition: $property $duration $animate $delay;
}

// Placeholder Mixins
@mixin placeholder {
  &.placeholder {
    @content;
  }
  &:-moz-placeholder {
    @content;
  }
  &::-moz-placeholder {
    @content;
  }
  &::-webkit-input-placeholder {
    @content;
  }
}

// Font family link
@import url('https://fonts.googleapis.com/css?family=Roboto:300i,400,400i,500,700,900');

.multi_step_form {
  background: #f6f9fb;
  display: block;
  overflow: hidden;

  #msform {
    text-align: center;
    position: relative;
    padding-top: 50px;
    min-height: 820px;
    max-width: 810px;
    margin: 0 auto;
    background: #ffffff;
    z-index: 1;

    .tittle {
      text-align: center;
      padding-bottom: 55px;

      h2 {
        font: 500 24px/35px $roboto;
        color: #3f4553;
        padding-bottom: 5px;
      }

      p {
        font: 400 16px/28px $roboto;
        color: $pfont;
      }
    }

    fieldset {
      border: 0;
      padding: 20px 105px 0;
      position: relative;
      left: 0;
      right: 0;

      &:not(:first-of-type) {
        display: none;
      }

      h3 {
        font: 500 18px/35px $roboto;
        color: #3f4553;
      }

      h6 {
        font: 400 15px/28px $roboto;
        color: $pfont;
        padding-bottom: 30px;
      }

      .intl-tel-input {
        display: block;
        background: transparent;
        border: 0;
        box-shadow: none;
        outline: none;

        .flag-container {
          .selected-flag {
            padding: 0 20px;
            background: transparent;
            border: 0;
            box-shadow: none;
            outline: none;
            width: 65px;

            .iti-arrow {
              border: 0;

              &:after {
                content: "\f35f";
                position: absolute;
                top: 0;
                right: 0;
                font: normal normal normal 24px/7px Ionicons;
                color: $pfont;
              }
            }
          }
        }
      }

      #phone {
        padding-left: 80px;
      }

      .form-group {
        padding: 0 10px;
      }

      .fg_2, .fg_3 {
        padding-top: 10px;
        display: block;
        overflow: hidden;
      }

      .fg_3 {
        padding-bottom: 70px;
      }

      .form-control, .product_select {
        border-radius: 3px;
        border: 1px solid #d8e1e7;
        padding: 0 20px;
        height: auto;
        font: 400 15px/48px $roboto;
        color: $pfont;
        box-shadow: none;
        outline: none;
        width: 100%;
        @include placeholder {
          color: $pfont;
        }

        &:hover, &:focus {
          border-color: $bc;
        }

        &:focus {
          @include placeholder {
            color: transparent;
          }
        }
      }

      .product_select {
        &:after {
          display: none;
        }

        &:before {
          content: "\f35f";
          position: absolute;
          top: 0;
          right: 20px;
          font: normal normal normal 24px/48px Ionicons;
          color: $pfont;
        }

        .list {
          width: 100%;
        }
      }

      .done_text {
        padding-top: 40px;

        .don_icon {
          height: 36px;
          width: 36px;
          line-height: 36px;
          font-size: 22px;
          margin-bottom: 10px;
          background: $bc;
          display: inline-block;
          border-radius: 50%;
          color: #ffffff;
          text-align: center;
        }

        h6 {
          line-height: 23px;
        }
      }

      .code_group {
        margin-bottom: 60px;

        .form-control {
          border: 0;
          border-bottom: 1px solid #a1a7ac;
          border-radius: 0;
          display: inline-block;
          width: 30px;
          font-size: 30px;
          color: $pfont;
          padding: 0;
          margin-right: 7px;
          text-align: center;
          line-height: 1;
        }
      }

      .passport {
        margin-top: -10px;
        padding-bottom: 30px;
        position: relative;

        .don_icon {
          height: 36px;
          width: 36px;
          line-height: 36px;
          font-size: 22px;
          position: absolute;
          top: 4px;
          right: 0;
          background: $bc;
          display: inline-block;
          border-radius: 50%;
          color: #ffffff;
          text-align: center;
        }

        h4 {
          font: 500 15px/23px $roboto;
          color: $pfont;
          padding: 0;
        }
      }

      .input-group {
        padding-bottom: 40px;

        .custom-file {
          width: 100%;
          height: auto;

          .custom-file-label {
            width: 168px;
            border-radius: 5px;
            cursor: pointer;
            font: 700 14px/40px $roboto;
            border: 1px solid #99a2a8;
            text-align: center;
            @include transition;
            color: $pfont;

            i {
              font-size: 20px;
              padding-right: 10px;
            }

            &:hover, &:focus {
              background: $bc;
              border-color: $bc;
              color: #fff;
            }
          }

          input {
            display: none;
          }
        }
      }

      .file_added {
        text-align: left;
        padding-left: 190px;
        padding-bottom: 60px;

        li {
          font: 400 15px/28px $roboto;
          color: $pfont;

          a {
            color: $bc;
            font-weight: 500;
            display: inline-block;
            position: relative;
            padding-left: 15px;

            i {
              font-size: 22px;
              padding-right: 8px;
              position: absolute;
              left: 0;
              transform: rotate(20deg);
            }
          }
        }
      }
    }

    #progressbar {
      margin-bottom: 30px;
      overflow: hidden;

      li {
        list-style-type: none;
        color: #99a2a8;
        font-size: 12px;
        width: calc(100% / 3);
        float: left;
        position: relative;
        font: 500 13px $roboto;

        &:nth-child(2) {
          &:before {
            content: url("./media/description.svg");
          }
        }

        &:nth-child(3) {
          &:before {
            content: url("./media/similarity-analysis.svg");
          }
        }

        &:before {
          content: url("./media/upload -image.svg");
          font: normal normal normal 50px/50px Ionicons;
          width: 50px;
          height: 50px;
          line-height: 50px;
          display: block;
          background: #eaf0f4;
          border-radius: 50%;
          margin: 0 auto 10px auto;
        }

        &:after {
          content: '';
          width: 100%;
          height: 10px;
          background: #eaf0f4;
          position: absolute;
          left: -50%;
          top: 21px;
          z-index: -1;
        }

        &:last-child {
          &:after {
            width: 150%;
          }
        }

        &.active {
          color: $bc;

          &:before, &:after {
            background: $bc;
            color: white;
          }
        }
      }
    }

    .action-button {
      background: $bc;
      color: white;
      border: 0 none;
      border-radius: 100px;
      cursor: pointer;
      min-width: 130px;
      font: 700 14px/40px $roboto;
      border: 1px solid $bc;
      margin: 0 5px;
      text-transform: uppercase;
      display: inline-block;

      &:hover, &:focus {
        background: $heding;
        border-color: $heding;
      }
    }

    .previous_button {
      background: transparent;
      color: #99a2a8;
      border-color: #99a2a8;

      &:hover, &:focus {
        background: $heding;
        border-color: $heding;
        color: #fff;
      }
    }
  }
}

</style>