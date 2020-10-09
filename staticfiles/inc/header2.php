<style>
	.main_menu a:hover {
    border-bottom: 2px solid #007bff;
    position: relative;
}
 .fa-spin-hover:hover {
   -webkit-animation: spin 2s;
   -moz-animation: spin 2s;
   -o-animation: spin 2s;
   animation: spin 2s;
}
@-moz-keyframes spin {
    from { -moz-transform: rotate(0deg); }
    to { -moz-transform: rotate(360deg); }
}
@-webkit-keyframes spin {
    from { -webkit-transform: rotate(0deg); }
    to { -webkit-transform: rotate(360deg); }
}
@keyframes spin {
    from {transform:rotate(0deg);}
    to {transform:rotate(360deg);}
}

</style>
<style>
.dropbtn {
    height: 30px;
    line-height: 30px;
    padding: 0 25px;
    background-color: #fcc741;
    -webkit-transition: all 0.3s linear;
    transition: all 0.3s linear;
    border: 0;
    color: #252628;
    font-weight: 600;
	border-radius: 15px;
	font-size:14px;
}
.dropdown {
  position: absolute;
  display: inline-block;
}

.dropdown-content {
  display: none;
  position: absolute;
  min-width:235px;
  z-index: 1;
    line-height:9px;
    padding: 0 25px;
    background-color: #fcc741;
    -webkit-transition: all 0.3s linear;
    transition: all 0.3s linear;
    border: 0;
    color: #252628;
    font-weight: 600;
	border-radius: 15px;
	font-size:14px;
}

.dropdown-content a {
  color: black;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
}
/*.dropdown-content a:hover {background-color: #007bff;}*/
.dropdown:hover .dropdown-content {display: block;}
.dropdown:hover .dropbtn {background-color: #007bff;}

.hr{
	margin-top: 2px!important;
	margin-bottom:2px !important;
}


.row.maega-menu {
    display: inline-block;}
.col-md-5.maega-menu-colum img {
	width: 100%;
	height: 176px;
	object-fit: cover;
	border: solid 3px whitesmoke;
	padding: 9px;
	border-radius: 4px;
	margin-left: -11px;
}
.dropdown-menu {
	width: 617px;
	line-height: 27px;
	padding: 23px;
}
.dropdown-menu li .sub-menu li > a.active,
.dropdown-menu li .sub-menu li:hover > a {
    color: #fcc741;
    padding-left: 20px;
}

.dropdown-menu li .sub-menu li a::before {
    display: none;
}

.dropdown-item {
    font-size: 15px;
    color: #595959;
    font-weight: 500;margin-left: -36px;
}
.dropdown-item:hover {
    color: #d5a440;
    background: transparent;
}
.navbar-expand .navbar-nav .dropdown-menu {
	position: absolute;
	top: 47px;
	border-top: solid 3px #01478c;
	left: 104px;
}
.dropdown-menu {
	width: 617px;
	line-height: 27px;
	padding: 23px;
	border: solid;top: 50px;
}
.dropdown-item {}

.dropdown-item li {
    margin-left: 20px;
    position: relative;
    display: inline-block;
}

.dropdown-item li:first-child {
    margin-left: 0;
}

.dropdown-item li a {
    padding: 0px 0;
    font-size: 14px;
    color: #fff;
    font-weight:800;
    position: relative;
    -webkit-transition: all 0.3s linear;
    transition: all 0.3s linear;
	letter-spacing:0.5px;
}


.dropdown-item li a i {
    font-size: 12px;
    margin-left: 5px;
}

.dropdown-item li > a.active,
.dropdown-item li:hover > a {
    color: #007bff;
}

.dropdown-item li .sub-menu {
    position: absolute;
    top: 110%;
    left: 0;
    width: 200px;
    background-color: #fff;
    opacity: 0;
    visibility: hidden;
    -webkit-transition: all 0.3s linear;
    transition: all 0.3s linear;
    z-index: 99;
    padding: 8px 0;
    box-shadow: 0px 0px 125px 0px rgba(0, 0, 0, 0.1);
}

.dropdown-item li .sub-menu li {
    margin: 0;
    display: block;
}

.dropdown-item li .sub-menu li a {
	display: block;
	padding: 8px 15px;
	color: #252628;
	-webkit-transition: all 0.3s linear;
	transition: all 0.3s linear;
	font-size: 14px;
	font-weight: 500;
}

.dropdown-item li .sub-menu li a i {
    float: right;
    line-height: 2;
}

.dropdown-item li .sub-menu li > a.active,
.dropdown-item li .sub-menu li:hover > a {
    color: #fcc741;
    padding-left: 20px;
}

.dropdown-item li .sub-menu li a::before {
    display: none;
}

.dropdown-item li:hover > .sub-menu {
    opacity: 1;
    top: 100%;
    visibility: visible;
}

.dropdown-item li .sub-menu li .sub-menu {
    top: 0;
    left: 100%;
}

.header_bottom_wrapper {
    background-color: #fff;
    padding: 0px;
}


@media all and (max-width:1200px){
	.dropdown-menu {
		line-height: 27px;
		padding: 23px;
		width: 495px;
		left: -100%;
	}
}
@media all and (max-width:1115px){

	.top-header .soicial_media img {
		width: 22px;
		margin-left: 5px;
	}
}
@media all and (max-width:991px){
	.nav-link{color:#fff; font-size: 15px;}
	.nav-link:hover{color:#fff; opacity: 0.8;}
	.menu .navbar.navbar-expand-lg {
		width: 100%;
	}
	.menu .navbar-toggler {
		/* float: right; */
		position: absolute;
		right: 0;
		top: 5px;
	}
	#navbarSupportedContent {
		text-align: start;
		position: absolute;
		top: 47px;
		background: #01478c;
		width: 100%;
		z-index: 9;
		padding: 15px 30px;
		left: 0;
	}
}

@media all and (max-width:960px){
	.top-header .col-md-3 {
		max-width: 250px;
		float: left;
		flex: 0 0 auto;
	}
	.top-header .col-md-9{
		position: absolute;
		flex: 0 0 auto;
		width:100%; max-width:100%;
	}

}


@media all and (max-width:575px){
	.navbar-nav .dropdown-menu {
		position: relative;
		float: none;
		left: 0;
		top: 0;
		max-width: 100%;
	}
}










</style>
	<div class="top d-none d-sm-block" style="width:100%; height:77px;">
		<div class="container-fluid" style="background-color: #323C4F;">
			<div class="row">
				<div class="col-sm-12">
					<div class="header_bottom_login">
						<ul style="margin-left: 32px;">
							<li class="ml2"><a href="#" style="color:#dee2e6ad;font-size: 12px;text-transform: uppercase;font-weight: 800;letter-spacing: 1px;padding:6px 0px 6px 0px;">+91 987 654 4321</a></li>
							<li><a href="#" style="color:#dee2e6ad;font-size: 12px;text-transform: uppercase;font-weight: 800;letter-spacing: 1px;padding:6px 0px 6px 0px;"><i class="fa fa-tags  fa-spin-hover"></i> COUPONS</a></li>
							<li><a href="#" style="color:#dee2e6ad;font-size: 12px;text-transform: uppercase;font-weight: 800;letter-spacing: 1px;padding:6px 0px 6px 0px;"><i class="fa fa-question  fa-spin-hover"></i> FQA</a></li>
							<li><a href="#" style="color:#dee2e6ad;font-size: 12px;text-transform: uppercase;font-weight: 800;letter-spacing: 1px;padding:6px 0px 6px 0px;"><i class="fa fa-newspaper-o  fa-spin-hover"></i> BLOG</a></li>
							<li><a href="#" style="color:#dee2e6ad;font-size: 12px;text-transform: uppercase;font-weight: 800;letter-spacing: 1px;padding:6px 0px 6px 0px;"><i class="fa fa-pencil    fa-spin-hover"></i> WRITE A REVIEW</a></li>
							<li><a href="#" style="color:#dee2e6ad;font-size: 12px;text-transform: uppercase;font-weight: 800;letter-spacing: 1px;padding:6px 0px 6px 0px;"><i class="fa fa-file-text-o  fa-spin-hover"></i> COMMON APPLICATION FORM</a></li>
							<li><a href="#" style="color:#dee2e6ad;font-size: 12px;text-transform: uppercase;font-weight: 800;letter-spacing: 1px;padding:6px 0px 6px 0px;"><i class="fa fa-book  fa-spin-hover"></i> TOP COURSES</a></li>
							<li><a href="#" style="color:#dee2e6ad;font-size: 12px;text-transform: uppercase;font-weight: 800;letter-spacing: 1px;padding:6px 0px 6px 0px;"><i class="fa fa-university  fa-spin-hover"></i> COLLEGES </a></li>
							<li><a href="#" style="color:#dee2e6ad;font-size: 12px;text-transform: uppercase;font-weight: 800;letter-spacing: 1px;padding:6px 0px 6px 0px;"><i class="fa fa-pencil-square-o  fa-spin-hover"></i> EXAMS</a></li>
						</ul>
					</div>
				</div>
			</div>
		</div>
		<div class="header_bottom_wrapper" style="position:relative;z-index: 9999;">
			<div class="row ">
				<div class="col-md-3 col-xs-12 pull-right">
					<div class="logo">
						<a href="#"><img src="assets/images/logo-2.png" style="height:45px;margin-top: 2px;margin-left: 32px;" alt="logo"></a>
					</div>
				</div>
				<div class="col-md-4 col-xs-12">
				</div>
				<div class="col-md-5 col-xs-12 float-right" style="margin-top:9px;padding-left: 170px;">
					<div class="header_bottom_login">
						<ul>
							<li>
								<div class="dropdown">
									<button class="dropbtn"><i class="fa fa-plus"></i> Add Institute / Business</button>
									<div class="dropdown-content">
										<a href="#">Schools</a>
										<hr class="hr">
										<a href="#">Colleges</a>
										<hr class="hr">
										<a href="#">Exams</a>
									</div>
								</div>
							</li>
							<li>
								<div class="dropdown">
									<button class="dropbtn"><i class="fa fa-user-o icon3"></i> Login</button>
									<!--div class="dropdown-content">
										<a href="#">Register</a>
									</div>-->
								</div>
							</li>
						</ul>
					</div>
				</div>				
			</div>
		</div>
	</div>
    <!--====== Header Desktop PART START ======-->
    <section class="header_area header_area_2 d-none d-lg-block" style="top:76px;">
        <div class="container">
            <div class="header_top_wrapper_2 d-flex justify-content-between">
                <div class="header_menu_3">
                    <ul class="main_menu">
                        <li>
                            <a class="active" href="index.html"><strong>Home</strong></a>
                        </li>
						<li>
                            <a  href="#">Schools <i class="fa fa-chevron-down"></i></a>
                            <ul class="sub-menu">
                                <li><a href="#">School Name</a></li>
                                <li><a href="#">School Name</a></li>
                            </ul>
                        </li>
						<li>
                            <a  href="#" data-toggle="dropdown">Schools <i class="fa fa-chevron-down"></i></a>
                            <ul class="dropdown-menu">
								<div class="row sub-menu">
									 <div class="col-md-3 maega-menu-colum">
										<ul>
											<a  class="dropdown-item" href="curtains.html">  Curtains  </a>
											<a class="dropdown-item" href="Blinds.html"> Blinds  </a>
											<a  class="dropdown-item" href="shuter.html"> Shutters    </a>
											<a class="dropdown-item" href="Awnings .html"> Awnings  </a>
											<a  class="dropdown-item" href="upholstry.html">Upholstery  </a>
										</ul>
									</div>
									<div class="col-md-3 maega-menu-colum">
										<ul>
											<a  class="dropdown-item" href="Bedheads.html">   Bedheads   </a>
											<a  class="dropdown-item" href="Bed-Covers .html">Bed Covers </a>
											<a  class="dropdown-item" href="cushion.html">   Cushion  </a>
											<a  class="dropdown-item" href="wallpaer.html">Wallpaper </a>  
											<a  class="dropdown-item" href="interiar.html">Interior Design </a>                        
										</ul>
									</div>
									<div class="col-md-1 maega-menu-colum"></div>
									<div class="col-md-5 maega-menu-colum">
										<img src="http://keenthemes.com/preview/metronic/theme/assets/global/plugins/jcrop/demos/demo_files/image1.jpg">								
									</div>
								</div>
							</ul>
                        </li>
						<li class=" dropdown">
							<a class="nav-link  " href="service.html" data-toggle="dropdown"> Our Services  <i class="fa fa-chevron-down"></i></a>
							<ul class="dropdown-menu">
								<div class="row submenu">
									 <div class="col-md-3 maega-menu-colum">
										<ul>
											<a  class="dropdown-item" href="curtains.html">  Curtains  </a>
											<a class="dropdown-item" href="Blinds.html"> Blinds  </a>
											<a  class="dropdown-item" href="shuter.html"> Shutters    </a>
											<a class="dropdown-item" href="Awnings .html"> Awnings  </a>
											<a  class="dropdown-item" href="upholstry.html">Upholstery  </a>
										</ul>
									</div>
									<div class="col-md-3 maega-menu-colum">
										<ul>
											<a  class="dropdown-item" href="Bedheads.html">   Bedheads   </a>
											<a  class="dropdown-item" href="Bed-Covers .html">Bed Covers </a>
											<a  class="dropdown-item" href="cushion.html">   Cushion  </a>
											<a  class="dropdown-item" href="wallpaer.html">Wallpaper </a>  
											<a  class="dropdown-item" href="interiar.html">Interior Design </a>                        
										</ul>
									</div>
									<div class="col-md-1 maega-menu-colum"></div>
									<div class="col-md-5 maega-menu-colum">
										<img src="http://keenthemes.com/preview/metronic/theme/assets/global/plugins/jcrop/demos/demo_files/image1.jpg">								
									</div>
								</div>
							</ul>
						</li>
						<li>
                            <a  href="#">Exams<i class="fa fa-chevron-down"></i></a>
                            <ul class="sub-menu">
                                <li><a href="#">Exam Name</a></li>
                                <li><a href="#">Exam Name</a></li>
                            </ul>
                        </li>
						<li>
                            <a  href="#">Courses<i class="fa fa-chevron-down"></i></a>

                            <ul class="sub-menu">
                                <li><a href="#">course Name</a></li>
                                <li><a href="#">course Name</a></li>
                            </ul>
                        </li>
						<li>
                            <a  href="#">Scholorships <i class="fa fa-chevron-down"></i></a>

                            <ul class="sub-menu">
                                <li><a href="#">Scholorship Name</a></li>
                                <li><a href="#">Scholorship Name</a></li>
                            </ul>
                        </li>
						<li>
                            <a  href="#">PG/Hostels<i class="fa fa-chevron-down"></i></a>

                            <ul class="sub-menu">
                                <li><a href="#">PG Name</a></li>
                                <li><a href="#">Hostel Name</a></li>
                            </ul>
                        </li>
						<li>
                            <a  href="#">Counselling<i class="fa fa-chevron-down"></i></a>
                            <ul class="sub-menu">
                                <li><a href="#">Counselling Name</a></li>
                                <li><a href="#">Counselling Name</a></li>
                            </ul>
                        </li>
						<li>
                            <a  href="#">More <i class="fa fa-chevron-down"></i></a>
                            <ul class="sub-menu">
                                <li><a href="#">Services Name</a></li>
                                <li><a href="#">Services Name</a></li>
                            </ul>
                        </li>
						<li>
                            <a href="#">Contact</a>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </section>
    <!--====== Header Desktop PART ENDS ======-->
    <!--====== Header Mobile PART START ======-->
    <section class="header_area header_area_2 d-lg-none">
        <div class="header_top">
            <div class="container">
                <div class="header_top_wrapper d-flex justify-content-center justify-content-md-between">
                    <div class="header_top_info d-none d-md-block">
                        <ul>
                            <li><img src="assets/images/call-2.png" alt="call"><a href="#">+91 458 654 528</a></li>
                            <li><img src="assets/images/mail-2.png" alt="mail"><a href="#">info@example.com</a></li>
                        </ul>
                    </div>
                    <div class="header_top_login">
                        <ul>
                            <li><a href="#">Create An Account</a></li>
                            <li><a class="main-btn" href="#"><i class="fa fa-user-o"></i> Log In</a></li>
							<li><a class="main-btn" href="#"><i class="fa fa-plus"></i> Add Institute / Business / Organisation</a></li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
        <div class="header_menu  header_mobile">
            <div class="container">
                <nav class="navbar navbar-expand-lg header_mobile_bg">
                    <a class="navbar-brand" href="index-3.html">
                        <img src="assets/images/logo-2.png" alt="logo">
                    </a>
                    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                        <span class="toggler-icon"></span>
                        <span class="toggler-icon"></span>
                        <span class="toggler-icon"></span>
                    </button>
                    <div class="collapse navbar-collapse sub-menu-bar" id="navbarSupportedContent">
                        <ul class="navbar-nav m-auto">
                            <li>
                                <a class="active" href="index.html">Home <i class="fa fa-chevron-down"></i></a>
                                
                                <ul class="sub-menu">
                                    <li><a href="index.html">Home 01</a></li>
                                    <li><a href="index-2.html">Home 02</a></li>
                                    <li><a class="active" href="index-3.html">Home 03</a></li>
                                    <li><a href="index-4.html">Home 04</a></li>
                                </ul>
                            </li>
                            <li>
                                <a href="about.html">About</a>
                            </li>
                            <li>
                                <a href="courses.html">Courses <i class="fa fa-chevron-down"></i></a>
                                
                                <ul class="sub-menu">
                                    <li><a href="courses.html">Courses</a></li>
                                    <li><a href="courses-details.html">Courses Details</a></li>
                                </ul>
                            </li>
                            <li>
                                <a href="blog.html">Blog <i class="fa fa-chevron-down"></i></a>
                                
                                <ul class="sub-menu">
                                    <li><a href="blog.html">Blog</a></li>
                                    <li><a href="blog-details.html">Blog Details</a></li>
                                </ul>
                            </li>
                            <li>
                                <a href="contact.html">Contact</a>
                            </li>
                        </ul>
                    </div>
                    <div class="navbar_meta">
                        <ul>
                            <li>
                                <a id="search" href="#"><img src="assets/images/search-2.png" alt="search"></a>
                                <div class="search_bar">
                                    <input type="text" placeholder="Search">
                                    <button><i class="fa fa-search"></i></button>
                                </div>
                            </li>
                            <li><a href="#"><img src="assets/images/cart-2.png" alt="cart"> <span>0</span></a></li>
                        </ul>
                    </div>
                </nav>
            </div>
        </div>
    </section>