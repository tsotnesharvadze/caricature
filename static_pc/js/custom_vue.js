function getCookie(cname) {
	var name = cname + "=";
	var ca = document.cookie.split(';');
	for (var i = 0; i < ca.length; i++) {
		var c = ca[i];
		while (c.charAt(0) == ' ') {
			c = c.substring(1);
		}
		if (c.indexOf(name) == 0) {
			return c.substring(name.length, c.length);
		}
	}
	return "";
}
var sections = new Vue({
	el: '#vue_body',
	// delimiters: ['{$', '$}'],
	data: {
        images:[],
        curent_page:1,
        previous_page:null,
        next_page:null,
	},
	created: function () {
        this.get_data();
		
	},
	methods: {
        nextPage: function(){
            if(this.next_page){
                this.curent_page ++;
                this.get_data();
            }
        },
        prevPage: function(){
            if(this.previous_page){
                this.curent_page --;
                this.get_data();
            }
        },
        get_data: function(){
            var self = this;
            jQuery.get("/API/karikaturebi/?format=json&page="+ self.curent_page, {}, function (dataa, status) {
                self.images = dataa.data;
                self.next_page = dataa.pagination.next;
                self.previous_page = dataa.pagination.previous;
            });
        }
	}

});


Vue.component('cimage', {
	props: ['image'],
    data:function(){
        return{
            inputDisabled: false,
            button_text: "დამატება",
        }
    },
    mounted:function(){
        this.inputDisabled = this.image.name.length > 3;
        console.log(this.image.name.length)
        this.button_text = this.image.name.length < 3 ? "დამატება" : "შენახულია";
    },
	methods: {
        saveName: function(){
            var self = this;
            jQuery.post(
                "/API/set_name/",
                {
                    "pk":this.image.pk,
                    "name": this.image.name,
                    'csrfmiddlewaretoken': getCookie('csrftoken'),
                },
                function(data){
                    self.inputDisabled = data.answer;
                    self.button_text = "შენახულია"
                }
            )
        }
	},
	template:`
    <div class="col-halfquart">
        <div class="each_item">
            <div class="each_item_in">
                <div class="image-block">
                    <img :src="image.get_image" alt="">
                </div>
                <div class="input-block">
                    <input type="text" v-model="image.name" :disabled="inputDisabled">
                </div>
                <div class="save-button">
                    <button @click="saveName" v-text="button_text"></button>
                </div>
            </div>
        </div>
    </div>`,
	
});