<style>
	.main_menu a:hover {
    position: relative;
	background-color:#007bff;
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
  position: relative;
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


.mega-dropdown {
  position: static !important;
}
.mega-dropdown-menu {
    padding: 20px 0px;
    width: 100%;
    box-shadow: none;
    -webkit-box-shadow: none;
}
.mega-dropdown-menu > li > ul {
  padding: 0;
  margin: 0;
}
.mega-dropdown-menu > li > ul > li {
  list-style: none;
}
.mega-dropdown-menu > li > ul > li > a {
  display: block;
  color: #222;
  padding: 3px 5px;
}
.mega-dropdown-menu > li ul > li > a:hover,
.mega-dropdown-menu > li ul > li > a:focus {
  text-decoration: none;
}
.mega-dropdown-menu .dropdown-header {
  font-size: 18px;
  color: #ff3546;
  padding: 5px 60px 5px 5px;
  line-height: 30px;
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
    <section class="header_area header_area_2 d-none d-lg-block collapse navbar-collapse js-navbar-collapse" style="top:76px;">
        <div class="container">
            <div class="header_top_wrapper_2 d-flex justify-content-between">
                <div class="header_menu_3">
                    <ul class="main_menu nav">
                        <li>
                            <a class="active" href="index.php"><strong>Home</strong></a>
                        </li>
						<li>
                            <a  href="#">Schools <i class="fa fa-chevron-down"></i></a>
                            <ul class="sub-menu">
                                <li><a href="#">School Name</a></li>
                                <li><a href="#">School Name</a></li>
                            </ul>
                        </li>
						<!--<li class="dropdown mega-dropdown row">
							<a href="#" class="dropdown-toggle" data-toggle="dropdown">Men <i class="fa fa-chevron-down"></i></span></a>				
							<ul class="dropdown-menu mega-dropdown-menu">
								<div class="row">
								<li class="col-sm-3">
									<ul>
										<li class="dropdown-header">Men Collection</li>                            
										<li class="divider"></li>
										<li><a href="#">View all Collection <span class="glyphicon glyphicon-chevron-right pull-right"></span></a></li>
									</ul>
								</li>
								<li class="col-sm-3">
									<ul>
										<li class="dropdown-header">Features</li>
										<li><a href="#">Auto Carousel</a></li>
										<li><a href="#">Carousel Control</a></li>
										<li><a href="#">Left & Right Navigation</a></li>
										<li><a href="#">Four Columns Grid</a></li>
										<li class="divider"></li>
										<li class="dropdown-header">Fonts</li>
										<li><a href="#">Glyphicon</a></li>
										<li><a href="#">Google Fonts</a></li>
									</ul>
								</li>
								<li class="col-sm-3">
									<ul>
										<li class="dropdown-header">Plus</li>
										<li><a href="#">Navbar Inverse</a></li>
										<li><a href="#">Pull Right Elements</a></li>
										<li><a href="#">Coloured Headers</a></li>                            
										<li><a href="#">Primary Buttons & Default</a></li>							
									</ul>
								</li>
								<li class="col-sm-3">
									<ul>
										<li class="dropdown-header">Much more</li>
										<li><a href="#">Easy to Customize</a></li>
										<li><a href="#">Calls to action</a></li>
										<li><a href="#">Custom Fonts</a></li>
										<li><a href="#">Slide down on Hover</a></li>                         
									</ul>
								</li>
								</div>
							</ul>				
						</li>-->
						<li>
                            <a  href="#">Colleges <i class="fa fa-chevron-down"></i></a>

                            <ul class="sub-menu">
                                <li><a href="#">College Name</a></li>
                                <li><a href="#">College Name</a></li>
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
                    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
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
<script>
$(document).ready(function(){
    $(".dropdown").hover(            
        function() {
            $('.dropdown-menu', this).not('.in .dropdown-menu').stop(true,true).slideDown("500");
            $(this).toggleClass('open');        
        },
        function() {
            $('.dropdown-menu', this).not('.in .dropdown-menu').stop(true,true).slideUp("00");
            $(this).toggleClass('open');       
        }
    );
});
</script>