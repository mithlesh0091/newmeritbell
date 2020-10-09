	<style>
	.main_menu a:hover {
    border-bottom: 2px solid #007bff;
    position: relative;
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
  min-width: 160px;
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
</style>
	<div class="top d-none d-sm-block" style="width:100%; height:77px;">
		<div class="container-fluid" style="background-color: #323C4F;">
			<div class="row">
				<div class="col-sm-12">
					<div class="header_bottom_login">
						<ul>
							<li><a href="#" style="color:#8E8E8E;font-size: 12px;text-transform: uppercase;font-weight: 800;letter-spacing: 1px;padding:6px 0px 6px 0px;">COUPONS</a></li>
							<li><a href="#" style="color:#8E8E8E;font-size: 12px;text-transform: uppercase;font-weight: 800;letter-spacing: 1px;padding:6px 0px 6px 0px;">FQA</a></li>
							<li><a href="#" style="color:#8E8E8E;font-size: 12px;text-transform: uppercase;font-weight: 800;letter-spacing: 1px;padding:6px 0px 6px 0px;"> BLOG</a></li>
							<li><a href="#" style="color:#8E8E8E;font-size: 12px;text-transform: uppercase;font-weight: 800;letter-spacing: 1px;padding:6px 0px 6px 0px;">WRITE A REVIEW</a></li>
							<li><a href="#" style="color:#8E8E8E;font-size: 12px;text-transform: uppercase;font-weight: 800;letter-spacing: 1px;padding:6px 0px 6px 0px;">COMMON APPLICATION FORM</a></li>
							<li><a href="#" style="color:#8E8E8E;font-size: 12px;text-transform: uppercase;font-weight: 800;letter-spacing: 1px;padding:6px 0px 6px 0px;">TOP COURSES</a></li>
							<li><a href="#" style="color:#8E8E8E;font-size: 12px;text-transform: uppercase;font-weight: 800;letter-spacing: 1px;padding:6px 0px 6px 0px;">COLLEGES </a></li>
							<li><a href="#" style="color:#8E8E8E;font-size: 12px;text-transform: uppercase;font-weight: 800;letter-spacing: 1px;padding:6px 0px 6px 0px;">EXAMS</a></li>
						</ul>
					</div>
				</div>
			</div>
		</div>
		<div class="header_bottom_wrapper" style="position:relative;z-index: 9999;">
			<div class="row ">
				<div class="col-md-3 col-xs-12 pull-right">
					<div class="logo">
						<a href="#"><img src="assets/images/logo-2.png" style="height:45px;margin-top: 2px;" alt="logo"></a>
					</div>
				</div>
				<div class="col-md-4 col-xs-12">
				</div>
				<div class="col-md-5 col-xs-12 float-left" style="margin-top:9px;">
					<div class="header_bottom_login">
						<ul>
							<li>
								<div class="dropdown">
									<button class="dropbtn"><i class="fa fa-plus"></i> Add Institute / Business / Organisation</button>
									<div class="dropdown-content">
										<a href="#">Schools</a>
										<a href="#">Colleges</a>
										<a href="#">Exams</a>
									</div>
								</div>
							</li>
							<li>
								<div class="dropdown">
									<button class="dropbtn"><i class="fa fa-user-o"></i> Login</button>
									<div class="dropdown-content">
										<a href="#">Register</a>
									</div>
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
                            <a class="active" href="index.html">Home</a>
                        </li>
						<li>
                            <a  href="#">Schools <i class="fa fa-chevron-down"></i></a>
                            <ul class="sub-menu">
                                <li><a href="#">School Name</a></li>
                                <li><a href="#">School Name</a></li>
                            </ul>
                        </li>
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