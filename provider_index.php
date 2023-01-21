<?php
  $group_name = \App\Models\Group::where('id',Auth::user()->group_id)->first();
  $pro_check = Auth::user()->type;
?>

@extends('layouts.provider')
@section('css')

  @if($pro_check == 'individual')
    <style type="text/css">
      #progressbar li {
        width: 20%;
      }
    </style>
  @endif


  @if($pro_check == 'group')
    <style type="text/css">
      #progressbar li {
        width: 50%;
      }
    </style>
  @endif


<style>
    #sig-canvas , #sig-canvas2 {
        margin-top: 20px;
    }
    #signatureModal  .modal-content .modal-body ,#signatureModal2  .modal-content .modal-body {
        display: -webkit-box;
        display: -ms-flexbox;
        display: block;
        -webkit-box-pack: center;
        -ms-flex-pack: center;
        justify-content: center;
        -webkit-box-align: center;
        -ms-flex-align: center;
        align-items: center;
        height: 50vh !important;
        width: 100%;
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
        margin: 0;
        padding: 32px 16px;
        font-family: Helvetica, Sans-Serif;
    }

</style>

@endsection
@section('headerselect')
    <div class="iq-search-bar">
      <h5>{{$prc->business_name}}</h5>
    </div>
@endsection
@section('proider')
    <div class="iq-card-body">
        <div class="question-enrollment">
            <div class="content card">
              <form id="msform">
                @csrf
                <!-- progressbar -->
                <ul id="progressbar">
                  @if($pro_check != "individual")
                    <li class="active" id="account" class = "{{$pro_check != "individual" ? 'active' : ''}}"><strong>Practice Information</strong></li>
                  @endif
                  @if($pro_check != 'group')
                  <li id="personal" class = "{{$pro_check == "individual" ? 'active' : ''}}"><strong>Provider Information</strong></li>
                  <li id="contract"><strong>Contract</strong></li>
                  <li id="question"><strong>Confidential Questionaire</strong></li>
                  <li id="access"><strong>Online Access</strong></li>
                  @endif
                  <li id="signature"><strong>Authorization Signature</strong></li>
                  {{-- <li id="payment"><strong>Payment</strong></li> --}}
                </ul>

                @if($pro_check != "individual")

                <!-- PRACTICE INFORMATION -->
                <fieldset>
                  <section class="section_1 mb_30">
                    <div class="col-item">
                      <div class="inner-main-title">
                        <h2>PRACTICE INFORMATION</h2>
                      </div>
                    </div>
                      <table cellspacing="0" cellpadding="0">
                          <thead>
                            <tr>
                              <th colspan="4">Group/Organization Information</th>
                            </tr>
                          </thead>
                          <tbody>
                            <tr>
                              <td>Legal Business Name as Reported to the IRS</td>
                              <td colspan="3"><input type="text" class="pr_business_name" name="pr_business_name" value="{{$prc->business_name ?? ''}}" required></td>
                            </tr>
                            <tr>
                              <td>DBA Name</td>
                              <td colspan="3"><input type="text" class="pr_dba_name" name="pr_dba_name" value="{{$prc->dba_name ?? ''}}"></td>
                            </tr>
                            <tr>
                              <td>Tax Identification Number</td>
                              <td colspan="3"><input type="text" class="pr_tax_id" name="pr_tax_id" value="{{$prc->tax_id ?? ''}}"></td>
                            </tr>
                            <tr>
                              <td>Group NPI</td>
                              <td colspan="3"><input type="text" class="pr_npi" name="pr_npi" value="{{$prc->npi ?? ''}}"></td>
                            </tr>
                            <tr>
                              <td>Address</td>
                              <td colspan="3"><input type="text" class="pr_address" name="pr_address" value="{{$prc->address ?? ''}}"></td>
                            </tr>
                            <tr>
                              <td>City</td>
                              <td colspan="3"><input type="text" class="pr_city" name="pr_city" value="{{$prc->city ?? ''}}"></td>
                            </tr>
                            <tr>
                              <td>State</td>
                              <td>
                                <div class="input-area"> <input type="text" class="pr_state" name="pr_state" value="{{$prc->state ?? ''}}"></div>
                              </td>
                              <td> ZIP </td>
                              <td><input type="text" class="pr_zip" name="pr_zip" value="{{$prc->zip ?? ''}}"></td>
                            </tr>
                            <tr>
                              <td>Phone</td>
                              <td>
                                <div class="input-area"> <input type="text" maxlength="11" class="pr_phone_number" name="pr_phone_number" value="{{$prc->phone_number ?? ''}}"></div>
                              </td>
                              <td> Fax </td>
                              <td><input type="text" class="pr_fax" name="pr_fax" value="{{$prc->fax ?? ''}}"></td>
                            </tr>
                            <tr>
                              <td>Medicaid #</td>
                              <td colspan="3"><input type="text" class="pr_medicaid" name="pr_medicaid" value="{{$prc->medicaid ?? ''}}"></td>
                            </tr>
                            <tr>
                              <td>Age Limitations</td>
                              <td colspan="3"><input type="text" class="pr_age_limit" name="pr_age_limit" value="{{$prc->age_limit ?? ''}}"></td>
                            </tr>
                            <tr>
                              <td>Working Hours</td>
                              <td colspan="3"><input type="text" class="pr_working_hrs" name="pr_working_hrs" value="{{$prc->working_hrs ?? ''}}"></td>
                            </tr>
                            <tr>
                              <td>Language Spoken</td>
                              <td colspan="3"><input type="text" class="pr_language_spoken" name="pr_language_spoken" value="{{$prc->language_spoken ?? ''}}"></td>
                            </tr>
                            <tr>
                              <td>Group Start Date</td>
                              <td colspan="3"><input type="date" class="pr_group_start_date" name="pr_group_start_date" value="{{isset($prc->group_start_date) ? \Carbon\Carbon::parse($prc->group_start_date)->format('Y-m-d') : ''}}"></td>
                            </tr>
                            <tr>
                              <td>Company Website</td>
                              <td colspan="3"><input type="text" class="pr_company_website" name="pr_company_website" value="{{$prc->company_website ?? ''}}"></td>
                            </tr>
                          </tbody>
                      </table>
                  </section>
                  {{-- PRACTICE DOCUMENTS SECTION --}}
                  <section class="section_2 mb_30">
                    <table>
                      <thead>
                        <tr>
                          <th colspan="3">Please upload copy of following documents (If available)</th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr>
                          <td>
                            <p>Signed W9</p>
                              <div class="d-flex justify-content-center">
                                <div class="mr-2">
                                  <label for="signw" class="btn btn-green"><i class="fa fa-upload mr-0 text-white" aria-hidden="true"></i></label>
                                  <input type="file" id="signw" class="up_file d-none" data-id="signw" data-type="Signed W9" multiple>
                                </div>
                                <?php
                                  $check = \App\Models\provider_document::where('group_id', Auth::user()->group_id)->where('doc_type', 'Signed W9')->where('provider_id', Auth::user()->id)->first();
                                ?>
                                @if($check)
                                <label class="btn btn-danger">
                                    <a href="{{route('download.practice.docs.save','Signed W9')}}" target="_blank"><i class="fa fa-download mr-0 text-white" aria-hidden="true"></i>
                                  </a>
                                </label>
                                @endif
                              </div>
                          </td>
                          <td>
                            <p>Liability Insurance</p>
                            <div class="d-flex justify-content-center">
                              <div class="mr-2">
                                <label for="liability" class="btn btn-green"><i class="fa fa-upload mr-0 text-white" aria-hidden="true"></i></label>
                                <input type="file" id="liability" class="up_file d-none" data-id="liability" data-type="Liability Insurance" multiple>
                              </div>
                              <?php
                                $check = \App\Models\provider_document::where('group_id', Auth::user()->group_id)->where('doc_type', 'Liability Insurance')->where('provider_id', Auth::user()->id)->first();
                              ?>
                              @if($check)
                                <div>
                                  <label class="btn btn-danger">
                                    <a href="{{route('download.practice.docs.save','Liability Insurance')}}" target="_blank"><i class="fa fa-download mr-0 text-white" aria-hidden="true"></i>
                                    </a>
                                  </label>
                                </div>
                              @endif
                            </div>
                          </td>
                          <td>
                            <p>CP-575 or appropriate substitute (or any letter from IRS)</p>
                            <div class="d-flex justify-content-center">
                              <div class="mr-2">
                                <label for="cp" class="btn btn-green"><i class="fa fa-upload mr-0 text-white" aria-hidden="true"></i></label>
                                <input type="file" id="cp" class="up_file d-none" data-id="cp" data-type="CP-575 or appropriate substitute" multiple>
                              </div>
                              <?php
                                $check = \App\Models\provider_document::where('group_id', Auth::user()->group_id)->where('doc_type', 'CP-575 or appropriate substitute')->where('provider_id', Auth::user()->id)->first();
                              ?>
                              @if($check)
                                <div>
                                  <label class="btn btn-danger">
                                    <a href="{{route('download.practice.docs.save','CP-575 or appropriate substitute')}}" target="_blank"><i class="fa fa-download mr-0 text-white" aria-hidden="true"></i>
                                    </a>
                                  </label>
                                </div>
                              @endif
                            </div>
                          </td>
                        </tr>
                        <tr>
                          <td>
                            <p>Certificate of incorporation (if corporation)</p>
                            <div class="d-flex justify-content-center">
                              <div class="mr-2">
                                <label for="incorporation" class="btn btn-green"><i class="fa fa-upload mr-0 text-white" aria-hidden="true"></i></label>
                                <input type="file" id="incorporation" class="up_file d-none" data-id="incorporation" data-type="Certificate of incorporation" multiple>
                              </div>
                              <?php
                                $check = \App\Models\provider_document::where('group_id', Auth::user()->group_id)->where('doc_type', 'Certificate of incorporation')->where('provider_id', Auth::user()->id)->first();
                              ?>
                              @if($check)
                                <div>
                                  <label class="btn btn-danger">
                                    <a href="{{route('download.practice.docs.save','Certificate of incorporation')}}" target="_blank"><i class="fa fa-download mr-0 text-white" aria-hidden="true"></i>
                                    </a>
                                  </label>
                                </div>
                              @endif
                            </div>
                          </td>
                          <td>
                            <p>Letter of intent</p>
                            <div class="d-flex justify-content-center">
                              <div class="mr-2">
                                <label for="letter" class="btn btn-green"><i class="fa fa-upload mr-0 text-white" aria-hidden="true"></i></label>
                                <input type="file" id="letter" class="up_file d-none" data-id="letter" data-type="Letter of Intent" multiple>
                              </div>
                              <?php
                                $check = \App\Models\provider_document::where('group_id', Auth::user()->group_id)->where('doc_type', 'Letter of Intent')->where('provider_id', Auth::user()->id)->first();
                              ?>
                              @if($check)
                                <div>
                                  <label class="btn btn-danger">
                                    <a href="{{route('download.practice.docs.save','Letter of Intent')}}" target="_blank"><i class="fa fa-download mr-0 text-white" aria-hidden="true"></i>
                                    </a>
                                  </label>
                                </div>
                              @endif
                            </div>
                          </td>
                          <td>
                            <p>Company Roster</p>
                            <div class="d-flex justify-content-center">
                              <div class="mr-2">
                                <label for="roster" class="btn btn-green"><i class="fa fa-upload mr-0 text-white" aria-hidden="true"></i></label>
                                <input type="file" id="roster" class="up_file d-none" data-id="roster" data-type="Company Roster" multiple>
                              </div>
                              <?php
                                $check = \App\Models\provider_document::where('group_id', Auth::user()->group_id)->where('doc_type', 'Company Roster')->where('provider_id', Auth::user()->id)->first();
                              ?>
                              @if($check)
                                <div>
                                  <label class="btn btn-danger">
                                    <a href="{{route('download.practice.docs.save','Company Roster')}}" target="_blank"><i class="fa fa-download mr-0 text-white" aria-hidden="true"></i>
                                    </a>
                                  </label>
                                </div>
                              @endif
                            </div>
                          </td>
                        </tr>
                        <tr>
                          <td>
                            <p>Competitive Advantages</p>
                            <div class="d-flex justify-content-center">
                              <div class="mr-2">
                                <label for="competitive" class="btn btn-green"><i class="fa fa-upload mr-0 text-white" aria-hidden="true"></i></label>
                                <input type="file" id="competitive" class="up_file d-none" data-id="competitive" data-type="Competitive Advantages" multiple>
                              </div>
                              <?php
                                $check = \App\Models\provider_document::where('group_id', Auth::user()->group_id)->where('doc_type', 'Competitive Advantages')->where('provider_id', Auth::user()->id)->first();
                              ?>
                              @if($check)
                                <div>
                                  <label class="btn btn-danger">
                                    <a href="{{route('download.practice.docs.save','Competitive Advantages')}}" target="_blank"><i class="fa fa-download mr-0 text-white" aria-hidden="true"></i>
                                    </a>
                                  </label>
                                </div>
                              @endif
                            </div>
                          </td>
                          <td colspan="2">
                            <p>Voided Check Copy</p>
                            <div class="d-flex justify-content-center">
                              <div class="mr-2">
                                <label for="voided" class="btn btn-green"><i class="fa fa-upload mr-0 text-white" aria-hidden="true"></i></label>
                                <input type="file" id="voided" class="up_file d-none" data-id="voided" data-type="Voided Check Copy" multiple>
                              </div>
                              <?php
                                $check = \App\Models\provider_document::where('group_id', Auth::user()->group_id)->where('doc_type', 'Voided Check Copy')->where('provider_id', Auth::user()->id)->first();
                              ?>
                              @if($check)
                                <div>
                                  <label class="btn btn-danger">
                                    <a href="{{route('download.practice.docs.save','Voided Check Copy')}}" target="_blank"><i class="fa fa-download mr-0 text-white" aria-hidden="true"></i>
                                    </a>
                                  </label>
                                </div>
                              @endif
                            </div>
                          </td>
                        </tr>
                      </tbody>
                    </table>

                    <div class="row" id="upload_div">

                    </div>
                  </section>
                  <button type="button" name="next" class="next action-button" value="Next" id="next_1">Save & Next <i class="fa fa-arrow-right" aria-hidden="true"></i></button>
                </fieldset>

                @endif
                @if($pro_check != "group")

                <!-- INDIVIDUAL PROVIDER INFORMATION -->
                <fieldset>
                  <section class="section_3 mb_30">
                    <div class="col-item">
                      <div class="inner-main-title">
                        <h2>INDIVIDUAL PROVIDER INFORMATION <br>
                          <span class="bracket">(Please make copy of this form if more than one individual provider)</span>
                        </h2>
                      </div>
                      <table cellspacing="0" cellpadding="0">

                        <tbody>
                          <tr>
                            <input type="hidden" name="pro_type" value="{{$pro_check}}">
                            <input type="hidden" name="check_save" value="provider_portal">
                            <input type="hidden" name="provider_id" value="{{$provider->provider->id ?? ''}}">
                            <td>First Name</td>
                            <td colspan="2"><input type="text" class="first_name" name="first_name" value="{{$provider->provider->first_name ?? ''}}" placeholder="Enter First Name"></td>
                            <td>Middle Name</td>
                            <td colspan="2"><input type="text" name="middle_name" value="{{$provider->provider->middle_name ?? ''}}" placeholder="Enter middle Name"></td>
                          </tr>
                          <tr>
                            <td>Last Name</td>
                            <td colspan="2"><input type="text" value="{{$provider->provider->last_name ?? ''}}" class="last_name" name="last_name" placeholder="Enter Last Name"></td>
                            <td>Suffix</td>
                            <td colspan="2"><input type="text" value="{{$provider->suffix}}" name="suffix" placeholder="Enter Suffix"></td>
                          </tr>
                          <tr>
                            <td>Date of Birth</td>
                            <td colspan="2"><input type="date" class="dob" name="dob" value="{{isset($provider->provider->dob) ? \Carbon\Carbon::parse($provider->provider->dob)->format('Y-m-d') : ''}}"></td>
                            <td>Gender</td>
                            <td colspan="2">
                              <div class="select-area">
                                <span>
                                    <input type="radio" id="male" name="gender"  {{$provider->provider->gender == "Male" ? 'checked' :''}} value="Male">
                                    <label for="male">Male</label>
                                </span>
                                <span>
                                    <input type="radio" id="female" name="gender"  {{$provider->provider->gender == "Female" ? 'checked' :''}} value="Female">
                                        <label for="female">Female</label>
                                </span>
                                </div>
                            </td>
                          </tr>

                          <tr>
                            <td>Speciality</td>
                            <td colspan="2">
                                <select class="form-control form-control-sm" class="speciality" name="speciality">
                                    <option value=""></option>
                                    @foreach($spec as $spe)
                                        <option value="{{$spe->speciality_name}}" {{$spe->speciality_name == $provider->speciality ? 'selected' : ''}}>{{$spe->speciality_name}}</option>
                                    @endforeach
                                </select>
                            </td>
                            <td>Taxonomy Code</td>
                            <td colspan="2"><input type="text" name="taxonomy_code" placeholder="Enter Taxonomy Code" value="{{$provider->taxonomy_code}}"></td>
                          </tr>

                          <tr>
                            <td>Tax Id</td>
                            <td colspan="2"><input type="text" class="tax_id" name="tax_id" placeholder="Enter Tax Id"
                                   value="{{$provider->tax_id}}"></td>
                            <td>SSN</td>
                            <td colspan="2"><input type="text" class="ssn" name="ssn" placeholder="Enter SSN"
                                   value="{{$provider->ssn}}"></td>
                          </tr>

                          <tr>
                            <td>NPI</td>
                            <td colspan="2"><input type="text" class="npi" name="npi" placeholder="Enter NPI"
                                   value="{{$provider->npi}}"></td>
                            <td>UPIN</td>
                            <td colspan="2"><input type="text" class="upin" name="upin" placeholder="Enter UPIN"
                                   value="{{$provider->upin}}"></td>
                          </tr>

                          <tr>
                            <td>DEA</td>
                            <td colspan="2"><input type="text" class="dea" name="dea" placeholder="Enter DEA"
                                   value="{{$provider->dea}}"></td>
                            <td>State License</td>
                            <td colspan="2"><input type="text" class="state_licence" name="state_licence" placeholder="Enter State License"
                                   value="{{$provider->state_licence}}"></td>
                          </tr>

                          <tr>
                            <td>Medicare PTAN</td>
                            <td colspan="2"><input type="text" name="medicare_ptan" placeholder="Enter Medicare PTAN" value="{{$provider->medicare_ptan}}"></td>
                            <td>Medicaid ID</td>
                            <td colspan="2"><input type="text" name="medicare_id" placeholder="Enter Medicaid ID" value="{{$provider->medicare_id}}"></td>
                          </tr>

                          <tr>
                            <td>Fax Number</td>
                            <td colspan="2"><input type="text" name="fax_number" placeholder="Enter Fax Number" value="{{$provider->fax_number}}"></td>
                            <td>Age Restriction</td>
                            <td colspan="2"><input type="text" name="age_restriction" placeholder="Enter Age Restriction" value="{{$provider->provider->age_restriction ?? ''}}"></td>
                          </tr>

                          <tr>
                            <td>Working Hours</td>
                            <td colspan="2"><input type="text" name="working_hours" placeholder="Enter Working Hours" value="{{$provider->provider->working_hours ?? ''}}"></td>
                            <td>County Name</td>
                            <td colspan="2"><input type="text" name="country_name" placeholder="Enter County Name" value="{{$provider->provider->country_name ?? ''}}"></td>
                          </tr>

                          <tr>
                            <td>Contact Manager</td>
                            <td colspan="2"><input type="text" name="contract_manager" placeholder="Enter Contact Manager"  value="{{$provider->provider->contract_manager ?? ''}}"></td>
                            <td>CAQH ID</td>
                            <td colspan="2"><input type="text" name="caqh_id" placeholder="Enter CAQH ID" value="{{$provider->provider->caqh_id ?? ''}}"></td>
                          </tr>

                          <tr>
                            <td>Phone</td>
                            <td colspan="2"><input type="text" class="phone" name="phone" placeholder="Enter Phone Number"
                                   value="{{$provider->provider->phone}}"></td>
                            <td>Email</td>
                            <td colspan="2"><input type="text" class="email" name="email" placeholder="Enter Email Address"
                                   value="{{$provider->provider->email ?? ''}}"></td>
                          </tr>

                          <tr>
                            <td>Address Name</td>
                            <td><input type="text" name="address_name" placeholder="Enter Address Name" value="{{$provider->provider->address_name ?? ''}}"></td>
                            <td>Street</td>
                            <td><input type="text" name="street" placeholder="Enter Street" value="{{$provider->provider->street ?? ''}}"></td>
                            <td>City</td>
                            <td><input type="text" name="city" placeholder="Enter City" value="{{$provider->provider->city ?? ''}}"></td>
                          </tr>

                          <tr>
                            <td>State</td>
                            <td colspan="2">
                              <select class="form-control form-control-sm" name="state">
                                <option>State</option>
                                <option value="AL" {{$provider->provider->state == "AL" ? 'selected' : ''}}>AL</option>
                                <option value="AK" {{$provider->provider->state == "AK" ? 'selected' : ''}}>AK</option>
                                <option value="AZ" {{$provider->provider->state == "AZ" ? 'selected' : ''}}>AZ</option>
                                <option value="AR" {{$provider->provider->state == "AR" ? 'selected' : ''}}>AR</option>
                                <option value="CA" {{$provider->provider->state == "CA" ? 'selected' : ''}}>CA</option>
                                <option value="CO" {{$provider->provider->state == "CO" ? 'selected' : ''}}>CO</option>
                                <option value="CT" {{$provider->provider->state == "CT" ? 'selected' : ''}}>CT</option>
                                <option value="DE" {{$provider->provider->state == "DE" ? 'selected' : ''}}>DE</option>
                                <option value="DC" {{$provider->provider->state == "DC" ? 'selected' : ''}}>DC</option>
                                <option value="FL" {{$provider->provider->state == "FL" ? 'selected' : ''}}>FL</option>
                                <option value="GA" {{$provider->provider->state == "GA" ? 'selected' : ''}}>GA</option>
                                <option value="HI" {{$provider->provider->state == "HI" ? 'selected' : ''}}>HI</option>
                                <option value="ID" {{$provider->provider->state == "ID" ? 'selected' : ''}}>ID</option>
                                <option value="IL" {{$provider->provider->state == "IL" ? 'selected' : ''}}>IL</option>
                                <option value="IN" {{$provider->provider->state == "IN" ? 'selected' : ''}}>IN</option>
                                <option value="IA" {{$provider->provider->state == "IA" ? 'selected' : ''}}>IA</option>
                                <option value="KS" {{$provider->provider->state == "KS" ? 'selected' : ''}}>KS</option>
                                <option value="KY" {{$provider->provider->state == "KY" ? 'selected' : ''}}>KY</option>
                                <option value="LA" {{$provider->provider->state == "LA" ? 'selected' : ''}}>LA</option>
                                <option value="ME" {{$provider->provider->state == "ME" ? 'selected' : ''}}>ME</option>
                                <option value="MD" {{$provider->provider->state == "MD" ? 'selected' : ''}}>MD</option>
                                <option value="MA" {{$provider->provider->state == "MA" ? 'selected' : ''}}>MA</option>
                                <option value="MI" {{$provider->provider->state == "MI" ? 'selected' : ''}}>MI</option>
                                <option value="MN" {{$provider->provider->state == "MN" ? 'selected' : ''}}>MN</option>
                                <option value="MS" {{$provider->provider->state == "MS" ? 'selected' : ''}}>MS</option>
                                <option value="MO" {{$provider->provider->state == "MO" ? 'selected' : ''}}>MO</option>
                                <option value="MT" {{$provider->provider->state == "MT" ? 'selected' : ''}}>MT</option>
                                <option value="NE" {{$provider->provider->state == "NE" ? 'selected' : ''}}>NE</option>
                                <option value="NV" {{$provider->provider->state == "NV" ? 'selected' : ''}}>NV</option>
                                <option value="NH" {{$provider->provider->state == "NH" ? 'selected' : ''}}>NH</option>
                                <option value="NJ" {{$provider->provider->state == "NJ" ? 'selected' : ''}}>NJ</option>
                                <option value="NM" {{$provider->provider->state == "NM" ? 'selected' : ''}}>NM</option>
                                <option value="NY" {{$provider->provider->state == "NY" ? 'selected' : ''}}>NY</option>
                                <option value="NC" {{$provider->provider->state == "NC" ? 'selected' : ''}}>NC</option>
                                <option value="ND" {{$provider->provider->state == "ND" ? 'selected' : ''}}>ND</option>
                                <option value="OH" {{$provider->provider->state == "OH" ? 'selected' : ''}}>OH</option>
                                <option value="OK" {{$provider->provider->state == "OK" ? 'selected' : ''}}>OK</option>
                                <option value="OR" {{$provider->provider->state == "OR" ? 'selected' : ''}}>OR</option>
                                <option value="PA" {{$provider->provider->state == "PA" ? 'selected' : ''}}>PA</option>
                                <option value="PR" {{$provider->provider->state == "PR" ? 'selected' : ''}}>PR</option>
                                <option value="RI" {{$provider->provider->state == "RI" ? 'selected' : ''}}>RI</option>
                                <option value="SC" {{$provider->provider->state == "SC" ? 'selected' : ''}}>SC</option>
                                <option value="SD" {{$provider->provider->state == "SD" ? 'selected' : ''}}> SD</option>
                                <option value="TN" {{$provider->provider->state == "TN" ? 'selected' : ''}}>TN</option>
                                <option value="TX" {{$provider->provider->state == "TX" ? 'selected' : ''}}>TX</option>
                                <option value="UT" {{$provider->provider->state == "UT" ? 'selected' : ''}}>UT</option>
                                <option value="VT" {{$provider->provider->state == "VT" ? 'selected' : ''}}>VT</option>
                                <option value="VA" {{$provider->provider->state == "VA" ? 'selected' : ''}}>VA</option>
                                <option value="WA" {{$provider->provider->state == "WA" ? 'selected' : ''}}>WA</option>
                                <option value="WV" {{$provider->provider->state == "WV" ? 'selected' : ''}}>WV</option>
                                <option value="WI" {{$provider->provider->state == "WI" ? 'selected' : ''}}>WI</option>
                                <option value="WY" {{$provider->provider->state == "WY" ? 'selected' : ''}}>WY</option>
                                <option value="AA" {{$provider->provider->state == "AA" ? 'selected' : ''}}>AA</option>
                                <option value="AE" {{$provider->provider->state == "AE" ? 'selected' : ''}}>AE</option>
                                <option value="AP" {{$provider->provider->state == "AP" ? 'selected' : ''}}>AP</option>
                                <option value="GU" {{$provider->provider->state == "GU" ? 'selected' : ''}}>GU</option>
                                <option value="VI" {{$provider->provider->state == "VI" ? 'selected' : ''}}>VI</option>
                                <option value="AB" {{$provider->provider->state == "AB" ? 'selected' : ''}}>AB</option>
                                <option value="BC" {{$provider->provider->state == "BC" ? 'selected' : ''}}>BC</option>
                                <option value="MB" {{$provider->provider->state == "MB" ? 'selected' : ''}}>MB</option>
                                <option value="NB" {{$provider->provider->state == "NB" ? 'selected' : ''}}>NB</option>
                                <option value="NL" {{$provider->provider->state == "NL" ? 'selected' : ''}}>NL</option>
                                <option value="NT" {{$provider->provider->state == "NT" ? 'selected' : ''}}>NT</option>
                                <option value="NS" {{$provider->provider->state == "NS" ? 'selected' : ''}}>NS</option>
                                <option value="NU" {{$provider->provider->state == "NU" ? 'selected' : ''}}>NU</option>
                                <option value="ON" {{$provider->provider->state == "ON" ? 'selected' : ''}}>ON</option>
                                <option value="PE" {{$provider->provider->state == "PE" ? 'selected' : ''}}>PE</option>
                                <option value="QC" {{$provider->provider->state == "QC" ? 'selected' : ''}}>QC</option>
                                <option value="SK" {{$provider->provider->state == "SK" ? 'selected' : ''}}>SK</option>
                                <option value="YT" {{$provider->provider->state == "YT" ? 'selected' : ''}}>YT</option>
                              </select>
                            </td>
                            <td>ZIP</td>
                            <td colspan="2"><input type="text" name="zip" placeholder="Enter ZIP" value="{{$provider->provider->zip ?? ''}}"></td>
                          </tr>

                          <tr>
                            <td>Start Date</td>
                            <td colspan="2"><input type="date" class="start_date" name="start_date" value="{{$provider->start_date}}"></td>
                            <td>End Date</td>
                            <td colspan="2"><input type="date" name="end_date" value="{{$provider->end_date}}"></td>
                          </tr>

                          <tr>
                            <td colspan="2">
                              <div class="custom-control custom-checkbox">
                                <input style="width: 20px;" type="checkbox" class="custom-control-input" id="Rendering-Provider" name="rp" value="1" {{$provider->rp == 1 ? 'checked' : ''}}>
                                <label class="custom-control-label" for="Rendering-Provider">Rendering Provider</label>
                              </div>
                            </td>
                            <td colspan="2">
                              <div class="custom-control custom-checkbox">
                                <input style="width: 20px;" type="checkbox" class="custom-control-input" id="Override-Company-Profile" name="ocp" value="1" {{$provider->ocp == 1 ? 'checked' : ''}}>
                                <label class="custom-control-label" for="Override-Company-Profile">Override Company Profile</label>
                              </div>
                            </td>
                            <td colspan="2">
                              <div class="custom-control custom-checkbox">
                                <input style="width: 20px;" type="checkbox" class="custom-control-input" id="Medicare-Participating" name="mp" value="1" {{$provider->mp == 1 ? 'checked' : ''}}>
                                <label class="custom-control-label" for="Medicare-Participating">Medicare Participating</label>
                              </div>
                            </td>
                          </tr>

                          <tr>
                            <td colspan="2">
                              <div class="custom-control custom-checkbox">
                                <input style="width: 20px;" type="checkbox" class="custom-control-input" id="Accepting-New-Patient" name="anp" value="1" {{$provider->anp == 1 ? 'checked' : ''}}>
                                <label class="custom-control-label" for="Accepting-New-Patient">Accepting New Patient</label>
                              </div>
                            </td>
                            <td colspan="2">
                              <div class="custom-control custom-checkbox">
                                <input style="width: 20px;" type="checkbox" class="custom-control-input" id="Printing-DEA-on-Prescription" name="pdop" value="1" {{$provider->pdop == 1 ? 'checked' : ''}}>
                                <label class="custom-control-label" for="Printing-DEA-on-Prescription">Printing DEA On Prescription</label>
                              </div>
                            </td>
                            <td colspan="2">
                              <div class="custom-control custom-checkbox">
                                <input style="width: 20px;" type="checkbox" class="custom-control-input" id="All-Payers-Participating" name="app" value="1" {{$provider->app == 1 ? 'checked' : ''}}>
                                <label class="custom-control-label" for="All-Payers-Participating">All Payers Participating</label>
                              </div>
                            </td>
                          </tr>
                        </tbody>
                      </table>
                    </div>
                  </section>
                  <button type="button" name="next" class="next action-button" value="Next" id="next_2">Save & Next <i class="fa fa-arrow-right" aria-hidden="true"></i></button>
                  @if($pro_check != "individual")
                    <button type="button" name="previous" class="previous action-button-previous" value="Previous"><i class="fa fa-arrow-left" aria-hidden="true"></i> Save & Previous</button>
                  @endif
                </fieldset>

                <!-- Contract -->
                <fieldset>
                  <div class="inner-main-title">
                    <h2>CONTRACT</h2>
                  </div>
                  <section id="contract_section">

                  </section>
                  <section id="new_contract_section">

                  </section>
                  <div class="row">
                    <button type="button" class="btn ml-auto mr-3 px-3 py-2 btn-green" id="add_contract"><i class="fa fa-plus mr-0" aria-hidden="true"></i>
                    </button>
                  </div>
                  <button type="button" name="next" class="next action-button" value="Next" id="next_5">    Save & Next
                      <i class="fa fa-arrow-right" aria-hidden="true"></i>
                  </button>
                  <button type="button" name="previous" class="previous action-button-previous" value="Previous">
                    <i class="fa fa-arrow-left" aria-hidden="true"></i> Save & Previous
                  </button>
                </fieldset>

                <!-- CONFIDENTIAL QUESTIONAIRE -->
                <fieldset>
                  <section class="section_4 mb_30">
                    <div class="col-item">
                      <div class="inner-main-title">
                        <h2>CONFIDENTIAL QUESTIONAIRE </h2>
                      </div>
                    </div>
                    <div class="col-item">
                      <div class="desc-text">
                        <P> <span class="bold-color">ATTENTION:</span> IF any of the following questions are answered “Yes”,
                          please
                          attach an explanation for
                          each answer. If any questions do not apply to you, please answer “No”. Failure to write an answer or
                          provide explanations for “Yes” answers, may delay the processing of your application.</P>
                      </div>
                    </div>



                    <div class="questions-answer-box mb_30">
                      <h3>LICENSURE INFORMATION:</h3>

                      <div class="question-box question-box1 mb_20">
                        <h4>1. Has your professional license ever been denied, limited, suspended, revoked, or subject to
                          probation
                          or
                          any other conditions in any state?</h4>
                        <ul>
                          <li class="group group_1"><input type="radio" id="yes1" name="c_license_expire" value="1" {{$qu->c_license_expire == 1 ? 'checked' : ''}}><label for="yes1">yes</label>
                          </li>
                          <li class="group group_2">
                            <input type="radio" id="no1" name="c_license_expire" value="2" {{$qu->c_license_expire == 2 ? 'checked' : ''}}><label for="no1">No</label>
                          </li>
                        </ul>
                        <div class="inner"><label>if yes, please explain:</label><br>
                          <div class="textarea-box">
                            <textarea rows="5" name="license_expire">{{$qu->license_expire}}</textarea>
                          </div>
                        </div>
                      </div>

                      <div class="question-box question-box2 mb_20">
                        <h4>2. Have you ever been disciplined, suspended, sanctioned, or otherwise restricted from participating
                          in
                          any private, Federal, or state health program (for example, Medicare, Medicaid), professional society,
                          MCO, state board of medical examiners, or professional conduct board?</h4>
                        <ul>
                          <li class="group group_1"><input type="radio" id="yes2" name="c_suspended" value="1" {{$qu->c_suspended == 1 ? 'checked' : ''}}><label for="yes2">yes</label>
                          </li>
                          <li class="group group_2">
                            <input type="radio" id="no2" name="c_suspended" value="2"><label for="no2" {{$qu->c_suspended == 2 ? 'checked' : ''}}>No</label>
                          </li>
                        </ul>
                        <div class="inner"><label>if yes, please explain:</label><br>
                          <div class="textarea-box">
                            <textarea rows="5" name="suspended">{{$qu->suspended}}</textarea>
                          </div>
                        </div>
                      </div>


                      <div class="question-box question-box3 mb_20">
                        <h4>3. Has your State Controlled Dangerous Substance (CDS) and/or your Federal DEA ever been limited,
                          restricted, reduced, suspended, revoked, denied, not renewed, or have you ever voluntarily surrendered
                          or
                          limited your registration with either/both of these agencies?</h4>
                        <ul>
                          <li class="group group_1"><input type="radio" id="yes3" name="c_cds" value="1" {{$qu->c_cds == 1 ? 'checked' : ''}}><label for="yes3">yes</label>
                          </li>
                          <li class="group group_2">
                            <input type="radio" id="no3" name="c_cds" value="2" {{$qu->c_cds == 2 ? 'checked' : ''}}><label for="no3">No</label>
                          </li>
                        </ul>
                        <div class="inner"><label>if yes, please explain:</label><br>
                          <div class="textarea-box">
                            <textarea rows="5" name="cds">{{$qu->cds}}</textarea>
                          </div>
                        </div>
                      </div>

                      <h3>CRIMINAL HISTORY:</h3>
                      <div class="question-box question-box4 mb_20">
                        <h4>4. Have you ever been indicted/convicted of a felony, or are you currently under investigation with
                          respect to such conduct?</h4>
                        <ul>
                          <li class="group group_1"><input type="radio" id="yes4" name="c_convicted" value="1" {{$qu->c_convicted == 1 ? 'checked' : ''}}><label for="yes4">yes</label>
                          </li>
                          <li class="group group_2">
                            <input type="radio" id="no4" name="c_convicted" value="2" {{$qu->c_convicted == 2 ? 'checked' : ''}}><label for="no4">No</label>
                          </li>
                        </ul>
                        <div class="inner"><label>if yes, please explain:</label><br>
                          <div class="textarea-box">
                            <textarea rows="5" name="convicted">{{$qu->convicted}}</textarea>
                          </div>
                        </div>
                      </div>

                      <h3>EDUCATION/TRAINING/BOARD CERTIFICATION:</h3>
                      <div class="question-box question-box5 mb_20">
                        <h4>5. During any period of your professional education, including but not limited to medical school,
                          internship, residency, fellowship, preceptor ship, or any other additional training, were you ever
                          disciplined, suspended, placed on probation, formally reprimanded, or asked to resign?</h4>
                        <ul>
                          <li class="group group_1"><input type="radio" id="yes5" name="c_edu" value="1" {{$qu->c_edu == 1 ? 'checked' : ''}}><label for="yes5">yes</label>
                          </li>
                          <li class="group group_2">
                            <input type="radio" id="no5" name="c_edu" value="2" {{$qu->c_edu == 2 ? 'checked' : ''}}><label for="no5">No</label>
                          </li>
                        </ul>
                        <div class="inner"><label>if yes, please explain:</label><br>
                          <div class="textarea-box">
                            <textarea rows="5" name="edu">{{$qu->edu}}</textarea>
                          </div>
                        </div>
                      </div>


                      <div class="question-box question-box6 mb_20">
                        <h4>6. Has your specialty board certification or eligibility ever been denied, revoked, relinquished,
                          not
                          renewed, or suspended?</h4>
                        <ul>
                          <li class="group group_1"><input type="radio" id="yes6" name="c_speciality" value="1" {{$qu->c_speciality == 1 ? 'checked' : ''}}><label for="yes6">yes</label>
                          </li>
                          <li class="group group_2">
                            <input type="radio" id="no6" name="c_speciality" value="2" {{$qu->c_speciality == 2 ? 'checked' : ''}}><label for="no6">No</label>
                          </li>
                        </ul>
                        <div class="inner"><label>if yes, please explain:</label><br>
                          <div class="textarea-box">
                            <textarea rows="5" name="d_speciality">{{$qu->speciality}}</textarea>
                          </div>
                        </div>
                      </div>


                      <div class="question-box question-box7 mb_20">
                        <h4>7. Have you ever chosen not to re-certify or voluntarily surrendered your board certification(s)
                          while
                          under investigation?</h4>
                        <ul>
                          <li class="group group_1"><input type="radio" id="yes7" name="c_recertify" value="1" {{$qu->c_recertify == 1 ? 'checked' : ''}}><label for="yes7">yes</label>
                          </li>
                          <li class="group group_2">
                            <input type="radio" id="no7" name="c_recertify" value="2" {{$qu->c_recertify == 2 ? 'checked' : ''}}><label for="no7">No</label>
                          </li>
                        </ul>
                        <div class="inner"><label>if yes, please explain:</label><br>
                          <div class="textarea-box">
                            <textarea rows="5" name="recertify">{{$qu->recertify}}</textarea>
                          </div>
                        </div>
                      </div>


                      <h3>INSURANCE INFORMATION:</h3>
                      <div class="question-box question-box8 mb_20">
                        <h4>8. Has any insurance carrier terminated, refused coverage, or rated up because of unusual risk or
                          have
                          any
                          procedures been excluded from your coverage?</h4>
                        <ul>
                          <li class="group group_1"><input type="radio" id="yes8" name="c_carrier" value="1" {{$qu->c_carrier == 1 ? 'checked' : ''}}><label for="yes8">yes</label>
                          </li>
                          <li class="group group_2">
                            <input type="radio" id="no8" name="c_carrier" value="2" {{$qu->c_carrier == 2 ? 'checked' : ''}}><label for="no8">No</label>
                          </li>
                        </ul>
                        <div class="inner"><label>if yes, please explain:</label><br>
                          <div class="textarea-box">
                            <textarea rows="5" name="carrier">{{$qu->carrier}}</textarea>
                          </div>
                        </div>
                      </div>

                      <div class="question-box question-box9 mb_20">
                        <h4>9. Are you currently uninsured for professional liability (malpractice insurance) coverage?</h4>
                        <ul>
                          <li class="group group_1"><input type="radio" id="yes9" name="c_uninsured" value="1" {{$qu->c_uninsured == 1 ? 'checked' : ''}}><label for="yes9">yes</label>
                          </li>
                          <li class="group group_2">
                            <input type="radio" id="no9" name="c_uninsured" value="2" {{$qu->c_uninsured == 2 ? 'checked' : ''}}><label for="no9">No</label>
                          </li>
                        </ul>
                        <div class="inner"><label>if yes, please explain:</label><br>
                          <div class="textarea-box">
                            <textarea rows="5" name="uninsured">{{$qu->uninsured}}</textarea>
                          </div>
                        </div>
                      </div>

                      <div class="question-box question-box10 mb_20">
                        <h4>10. Are you currently involved in any pending professional liability suits, claims, and/or actions?
                        </h4>
                        <ul>
                          <li class="group group_1"><input type="radio" id="yes10" name="c_liability" value="1" {{$qu->c_liability == 1 ? 'checked' : ''}}><label for="yes10">yes</label>
                          </li>
                          <li class="group group_2">
                            <input type="radio" id="no10" name="c_liability" value="2" {{$qu->c_liability == 2 ? 'checked' : ''}}><label for="no10">No</label>
                          </li>
                        </ul>
                        <div class="inner"><label>if yes, please explain:</label><br>
                          <div class="textarea-box">
                            <textarea rows="5" name="liability">{{$qu->liability}}</textarea>
                          </div>
                        </div>
                      </div>

                      <div class="question-box question-box11 mb_20">
                        <h4>11. Have any judgments ever been made against you in professional liability cases or claims, or have
                          you
                          ever entered into any settlements?</h4>
                        <ul>
                          <li class="group group_1"><input type="radio" id="yes11" name="c_judgement" value="1" {{$qu->c_judgement == 1 ? 'checked' : ''}}><label for="yes11">yes</label>
                          </li>
                          <li class="group group_2">
                            <input type="radio" id="no11" name="c_judgement" value="{{2}}" {{$qu->c_judgement == 2 ? 'checked' : ''}}><label for="no11">No</label>
                          </li>
                        </ul>
                        <div class="inner"><label>if yes, please explain:</label><br>
                          <div class="textarea-box">
                            <textarea rows="5" name="judgement">{{$qu->judgement}}</textarea>
                          </div>
                        </div>
                      </div>

                      <div class="question-box question-box12 mb_20">
                        <h4>12. To your knowledge, has information pertaining to you ever been reported to the National
                          Practitioner
                          Data Bank?</h4>
                        <ul>
                          <li class="group group_1"><input type="radio" id="yes12" name="c_npdb" value="1" {{$qu->c_npdb == 1 ? 'checked' : ''}}><label for="yes12">yes</label>
                          </li>
                          <li class="group group_2">
                            <input type="radio" id="no12" name="c_npdb" value="2" {{$qu->c_npdb == 2 ? 'checked' : ''}}><label for="no12">No</label>
                          </li>
                        </ul>
                        <div class="inner"><label>if yes, please explain:</label><br>
                          <div class="textarea-box">
                            <textarea rows="5" name="npdb">{{$qu->npdb}}</textarea>
                          </div>
                        </div>
                      </div>

                      <h3>HEALTH STATUS:</h3>
                      <div class="question-box question-box13 mb_20">
                        <h4>13. Do you currently have any medical, chemical dependency, or psychiatric conditions that might
                          adversely affect your ability to practice medicine or surgery or to perform the essential functions of
                          your
                          professional position?</h4>
                        <ul>
                          <li class="group group_1"><input type="radio" id="yes13" name="c_medical" value="1" {{$qu->c_medical == 1 ? 'checked' : ''}}><label for="yes13">yes</label>
                          </li>
                          <li class="group group_2">
                            <input type="radio" id="no13" name="c_medical" value="2" {{$qu->c_medical == 2 ? 'checked' : ''}}><label for="no13">No</label>
                          </li>
                        </ul>
                        <div class="inner"><label>if yes, please explain:</label><br>
                          <div class="textarea-box">
                            <textarea rows="5" name="medical">{{$qu->medical}}</textarea>
                          </div>
                        </div>
                      </div>


                      <div class="question-box question-box14 mb_20">
                        <h4>14. Are you currently participating in or under the supervision of a Physician or Recovery Network
                          or
                          any
                          other applicable recovery program?</h4>
                        <ul>
                          <li class="group group_1"><input type="radio" id="yes14" name="c_supervision" value="1" {{$qu->c_supervision == 1 ? 'checked' : ''}}><label for="yes14">yes</label>
                          </li>
                          <li class="group group_2">
                            <input type="radio" id="no14" name="c_supervision" value="2" {{$qu->c_supervision == 2 ? 'checked' : ''}}><label for="no14">No</label>
                          </li>
                        </ul>
                        <div class="inner"><label>if yes, please explain:</label><br>
                          <div class="textarea-box">
                            <textarea rows="5" name="supervision">{{$qu->supervision}}</textarea>
                          </div>
                        </div>
                      </div>

                      <h3>HOSPITAL/OTHER AFFILIATIONS:</h3>
                      <div class="question-box question-box15 mb_20">
                        <h4>15. Have your hospital and/or clinical privileges ever been limited, restricted, reduced, suspended,
                          revoked, denied, not renewed, or have you voluntarily surrendered or limited your privileges during or
                          under the threat of
                          investigation?</h4>
                        <ul>
                          <li class="group group_1"><input type="radio" id="yes15" name="15st" value="1" {{$qu->c_clinical == 1 ? 'checked' : ''}}><label for="yes15">yes</label>
                          </li>
                          <li class="group group_2">
                            <input type="radio" id="no15" name="15st" value="2" {{$qu->c_clinical == 2 ? 'checked' : ''}}><label for="no15">No</label>
                          </li>
                        </ul>
                        <div class="inner"><label>if yes, please explain:</label><br>
                          <div class="textarea-box">
                            <textarea rows="5" name="clinical">{{$qu->clinical}}</textarea>
                          </div>
                        </div>
                      </div>
                    </div>

                  </section>
                  <section class="section_5">
                    <table cellpadding="0" cellspacing="0">
                      <thead>
                        <th colspan="4">Please upload a copy of following documents</th>
                      </thead>
                      <tbody>
                        <tr>
                          <td>
                            <p>Resume (with exp.)</p>
                              <div class="d-flex justify-content-center">
                                <div class="mr-2">
                                  <label for="resume" class="btn btn-green"><i class="fa fa-upload mr-0 text-white" aria-hidden="true"></i></label>
                                  <input type="file" id="resume" class="up_file2 d-none" data-id="resume" data-type="Resume" multiple>
                                </div>
                                <?php
                                  $check = \App\Models\provider_document::where('group_id', Auth::user()->group_id)->where('doc_type', 'Resume')->where('provider_id', Auth::user()->id)->first();
                                ?>
                                @if($check)
                                <label class="btn btn-danger">
                                    <a href="{{route('download.practice.docs.save','Resume')}}" target="_blank"><i class="fa fa-download mr-0 text-white" aria-hidden="true"></i>
                                  </a>
                                </label>
                                @endif
                              </div>
                          </td>
                          <td>
                            <p>Copy of Degree</p>
                              <div class="d-flex justify-content-center">
                                <div class="mr-2">
                                  <label for="degree" class="btn btn-green"><i class="fa fa-upload mr-0 text-white" aria-hidden="true"></i></label>
                                  <input type="file" id="degree" class="up_file2 d-none" data-id="degree" data-type="Copy of Degree" multiple>
                                </div>
                                <?php
                                  $check = \App\Models\provider_document::where('group_id', Auth::user()->group_id)->where('doc_type', 'Copy of Degree')->where('provider_id', Auth::user()->id)->first();
                                ?>
                                @if($check)
                                <label class="btn btn-danger">
                                    <a href="{{route('download.practice.docs.save','Copy of Degree')}}" target="_blank"><i class="fa fa-download mr-0 text-white" aria-hidden="true"></i>
                                  </a>
                                </label>
                                @endif
                              </div>
                          </td>
                          <td>
                            <p>Board Certifications</p>
                              <div class="d-flex justify-content-center">
                                <div class="mr-2">
                                  <label for="board" class="btn btn-green"><i class="fa fa-upload mr-0 text-white" aria-hidden="true"></i></label>
                                  <input type="file" id="board" class="up_file2 d-none" data-id="board" data-type="Board Certifications" multiple>
                                </div>
                                <?php
                                  $check = \App\Models\provider_document::where('group_id', Auth::user()->group_id)->where('doc_type', 'Board Certifications')->where('provider_id', Auth::user()->id)->first();
                                ?>
                                @if($check)
                                <label class="btn btn-danger">
                                    <a href="{{route('download.practice.docs.save','Board Certifications')}}" target="_blank"><i class="fa fa-download mr-0 text-white" aria-hidden="true"></i>
                                  </a>
                                </label>
                                @endif
                              </div>
                          </td>
                          <td>
                            <p>Copy of State License</p>
                              <div class="d-flex justify-content-center">
                                <div class="mr-2">
                                  <label for="license" class="btn btn-green"><i class="fa fa-upload mr-0 text-white" aria-hidden="true"></i></label>
                                  <input type="file" id="license" class="up_file2 d-none" data-id="license" data-type="Copy of State License" multiple>
                                </div>
                                <?php
                                  $check = \App\Models\provider_document::where('group_id', Auth::user()->group_id)->where('doc_type', 'Copy of State License')->where('provider_id', Auth::user()->id)->first();
                                ?>
                                @if($check)
                                <label class="btn btn-danger">
                                    <a href="{{route('download.practice.docs.save','Copy of State License')}}" target="_blank"><i class="fa fa-download mr-0 text-white" aria-hidden="true"></i>
                                  </a>
                                </label>
                                @endif
                              </div>
                          </td>
                        </tr>
                        <tr>
                          <td>
                            <p>Liability Insurance</p>
                              <div class="d-flex justify-content-center">
                                <div class="mr-2">
                                  <label for="liability_ins" class="btn btn-green"><i class="fa fa-upload mr-0 text-white" aria-hidden="true"></i></label>
                                  <input type="file" id="liability_ins" class="up_file2 d-none" data-id="liability_ins" data-type="Liability Insurance" multiple>
                                </div>
                                <?php
                                  $check = \App\Models\provider_document::where('group_id', Auth::user()->group_id)->where('doc_type', 'Liability Insurance')->where('provider_id', Auth::user()->id)->first();
                                ?>
                                @if($check)
                                <label class="btn btn-danger">
                                    <a href="{{route('download.practice.docs.save','Liability Insurance')}}" target="_blank"><i class="fa fa-download mr-0 text-white" aria-hidden="true"></i>
                                  </a>
                                </label>
                                @endif
                              </div>
                          </td>
                          <td>
                            <p>Additional License and other certificates</p>
                              <div class="d-flex justify-content-center">
                                <div class="mr-2">
                                  <label for="add_license" class="btn btn-green"><i class="fa fa-upload mr-0 text-white" aria-hidden="true"></i></label>
                                  <input type="file" id="add_license" class="up_file2 d-none" data-id="add_license" data-type="Additional License and other certificates" multiple>
                                </div>
                                <?php
                                  $check = \App\Models\provider_document::where('group_id', Auth::user()->group_id)->where('doc_type', 'Additional License and other certificates')->where('provider_id', Auth::user()->id)->first();
                                ?>
                                @if($check)
                                <label class="btn btn-danger">
                                    <a href="{{route('download.practice.docs.save','Additional License and other certificates')}}" target="_blank"><i class="fa fa-download mr-0 text-white" aria-hidden="true"></i>
                                  </a>
                                </label>
                                @endif
                              </div>
                          </td>
                          <td colspan="2">
                            <p>Provider Affiliation With Group</p>
                              <div class="d-flex justify-content-center">
                                <div class="mr-2">
                                  <label for="pro_aff" class="btn btn-green"><i class="fa fa-upload mr-0 text-white" aria-hidden="true"></i></label>
                                  <input type="file" id="pro_aff" class="up_file2 d-none" data-id="pro_aff" data-type="Provider Affiliation With Group" multiple>
                                </div>
                                <?php
                                  $check = \App\Models\provider_document::where('group_id', Auth::user()->group_id)->where('doc_type', 'Provider Affiliation With Group')->where('provider_id', Auth::user()->id)->first();
                                ?>
                                @if($check)
                                <label class="btn btn-danger">
                                    <a href="{{route('download.practice.docs.save','Provider Affiliation With Group')}}" target="_blank"><i class="fa fa-download mr-0 text-white" aria-hidden="true"></i>
                                  </a>
                                </label>
                                @endif
                              </div>
                          </td>
                        </tr>
                      </tbody>
                    </table>

                    <div id="upload_div2"></div>

                  </section>
                  <br><br>
                  {{-- <section class="section_6">
                    <div class="col-item">
                      <div class="desc-text">
                        <p>I confirm that all information is accurate and complete to the best of my knowledge and ability. . I
                          permit Amromed LLC to use this information and extrapolate into every form which they
                          fill on my behalf.</p>
                      </div>
                      <br>
                      <div class="signature-box flex-div">
                        <div class="col-item signature-box">
                          <div class="col-item">
                            <span><input id="provider-sign" type="text" data-toggle="modal"
                                data-target="#signatureModal"></span>
                            <span><label for="provider-sign">Provider Signature:</label></span>
                          </div>
                        </div>
                        <div class="col-item">
                          <span><input id="provider-date" type="date" name="signature_date"></span>
                          <span><label for="provider-date">Date:</label></span>
                        </div>
                      </div>
                    </div>
                  </section> --}}
                  <button type="button" name="next" class="next action-button" value="Next" id="next_3" >Save & Next <i class="fa fa-arrow-right" aria-hidden="true"></i></button>
                  <button type="button"
                    name="previous" class="previous action-button-previous" value="Previous"><i class="fa fa-arrow-left" aria-hidden="true"></i> Save & Previous</button>
                </fieldset>

                <!-- Online Access -->
                <fieldset>
                  <section class="mb_30">
                    <div class="col-item">
                      <div class="inner-main-title">
                        <h2>ONLINE ACCESS</h2>
                      </div>
                      <div class="float-right">
                        <a href="#addAccess" class="btn btn-sm btn-primary mb-3" data-toggle="modal"><i class="fa fa-plus mr-0" aria-hidden="true"></i></a>
                    </div>
                    <!-- table -->
                    <div class="table-responsive online_table" id="online_table">

                  </div>
                    </div>
                  </section>
                  <button type="button" name="next" class="next action-button" value="Next">Save & Next <i
                    class="fa fa-arrow-right" aria-hidden="true"></i></button>
                  <button type="button" name="previous" class="previous action-button-previous" value="Previous"><i
                    class="fa fa-arrow-left" aria-hidden="true"></i>Save & Previous</button>
                </fieldset>

                @endif

                <!-- Authorization Signature -->
                <fieldset>
                  <div class="author-signature">
                    <div class="inner-content">
                      <div class="page-title">
                        <h1>Authorization for use of signature</h1>
                      </div>
                      <section class="section_2">
                        <div class="col-item mb_40">
                          <p>I, <span><input type="text" value="{{$auth->name}}" name="name"></span>, authorize <strong> {{$group_name->group_name}}</strong> to use my below signed
                            “sample signatures” as a representative of <span><input type="text" name="company_name" value="{{$auth->company_name}}"></span> on the
                            forms/applications of
                            different insurance companies/Medical Groups used for the purpose of Enrollment/Contracting only.
                          </p>
                        </div>
                        <div class="flex-div">
                          <div class="col-item signature-box">
                            <table cellspacing="0" cellpadding="0">
                              <thead>
                                <tr>
                                  <td colspan="2"> <strong> Signature for Authorization </strong> <br>
                                    <span class="bracket">(Attach the signatures below)</span></td>
                                </tr>
                                <tr>
                                  <td colspan="2">
                                    @if(!empty($auth->authorization_signature) && file_exists($auth->authorization_signature))
                                      <img src="{{asset('/').$auth->authorization_signature}}" class="img-fluid" id="sig_img">
                                    @elseif(!empty($provider->sig_file) && file_exists($provider->sig_file))
                                       <img src="{{asset($provider->sig_file)}}" id="sig_img" class="img-fluid">
                                    @endif
                                    <span><input id="author-sign" type="text" name="Signature" data-toggle="modal" data-target="#signatureModal"></span> <p>Signature for Authorization</p>
                                  </td>
                                </tr>
                              </thead>
                            </table>
                          </div>
                          {{-- <div class="col-item">
                            <span><input id="author-sign" type="text" name="Signature" data-toggle="modal"
                                data-target="#signatureModal2"></span>
                            <p>Signature for Authorization</p>
                          </div> --}}
                        </div>
                      </section>
                    </div>
                  </div>
                  <button type="button" name="next" class="action-button" id="next_4">Submit <i class="fa fa-check" aria-hidden="true"></i></button>
                  <button type="button"
                    name="previous" class="previous action-button-previous" value="Previous"><i class="fa fa-arrow-left" aria-hidden="true"></i> Previous</button>
                </fieldset>

            </div>
        </div>
            <div class="modal fade" id="signatureModal" data-backdrop="static">
                <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
                  <div class="modal-content">
                    <div class="modal-header">
                      <h4>Add signature</h4>
                      <button type="button" class="close" data-dismiss="modal">&times;</button>
                    </div>
                    <div class="modal-body" style="min-height: 400px;">
                      <ul class="nav nav-tabs">
                        <li class="nav-item">
                          <button class="nav-link active" data-toggle="tab" data-target="#drawsig" type="button" role="tab"
                            aria-controls="drawsig" aria-selected="true">Draw</button>
                        </li>
                        <li class="nav-item">
                          <button class="nav-link" data-toggle="tab" data-target="#uploadsig" type="button" role="tab"
                            aria-controls="uploadsig" aria-selected="false">Upload</button>
                        </li>
                      </ul>
                      <div class="tab-content">
                        <div class="tab-pane fade show active" id="drawsig" role="tabpanel">
                          <div class="row mb-2">
                            <div class="col-md-12">
                              <canvas id="sig-canvas" height="120" style="width: 100%;"></canvas>
                            </div>
                            <input type="hidden" class="form-control-file sign1" name="sign1">
                          </div>
                          <button type="button" class="btn btn-danger p-2" id="sig-clearBtn">Clear</button>
                        </div>
                        <div class="tab-pane fade" id="uploadsig" role="tabpanel">
                          <label class="upload-file-heading">Upload File</label>
                          <input type="file" class="form-control-file file1" name="file1">
                        </div>
                      </div>
                    </div>
                    <div class="modal-footer">
                        <button type="submit" class="btn btn-outline-primary" id="add_sig1" data-dismiss="modal"> Add Signature
                        </button>
                      <button type="button" class="btn btn-danger" data-dismiss="modal">Cancel</button>
                    </div>
                  </div>
                </div>
            </div>

            <div class="modal fade" id="signatureModal2" data-backdrop="static">
                <div class="modal-dialog modal-dialog-scrollable modal-dialog-centered">
                    <form method="post" id="client_sing_form_provider" enctype="multipart/form-data">
                        @csrf
                        <div class="modal-content">
                            <div class="modal-header">
                                <h4>Add signature</h4>
                                <button type="button" class="close" data-dismiss="modal">&times;</button>
                            </div>
                            <div class="modal-body">
                                <ul class="nav nav-tabs">
                                    <li class="nav-item">
                                        <a class="nav-link active" data-toggle="tab" href="#drawsig1">Draw</a>
                                    </li>
                                    <li class="nav-item">
                                        <a class="nav-link" data-toggle="tab" href="#uploadsig1">Upload</a>
                                    </li>
                                </ul>
                                <div class="tab-content">
                                    <div class="tab-pane fade show active" id="drawsig1">
                                        <div class="row mb-2">
                                            <div class="col-md-12">
                                                <canvas id="sig-canvas2" height="120" style="width: 100%;"></canvas>
                                            </div>
                                            <input type="hidden" class="form-control-file sign2" name="sign2">
                                        </div>
                                        <button type="button" class="btn btn-danger p-2" id="sig-clearBtn2">
                                            Clear
                                        </button>
                                    </div>
                                    <div class="tab-pane fade" id="uploadsig1">
                                        <label>Upload File</label>
                                        <input type="file" class="form-control-file" name="file2">
                                    </div>
                                </div>
                            </div>
                            <div class="modal-footer">
                                <button type="submit" class="btn btn-outline-primary" id="add_sig2" data-dismiss="modal"> Add Signature </button>
                                <button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
                            </div>
                        </div>
                    </form>
                </div>
            </div>

            <!-- Add Access Modal -->
            <div class="modal fade" id="addAccess" data-backdrop="static">
              <div class="modal-dialog modal-dialog-scrollable modal-dialog-centered">
                  <div class="modal-content">
                      <div class="modal-header">
                          <h4>Add Access</h4>
                          <button type="button" class="close"
                              data-dismiss="modal">&times;</button>
                      </div>
                      <form action="#">
                          <div class="modal-body">
                              <div class="row">
                                  <div class="col-md-4 mb-2">
                                      <label>Access Name</label>
                                  </div>
                                  <div class="col-md-8 mb-2">
                                      <input type="text" class="form-control form-control-sm"
                                          required name="a_name" id="a_name">
                                  </div>
                                  <div class="col-md-4 mb-2">
                                      <label>URL</label>
                                  </div>
                                  <div class="col-md-8 mb-2">
                                      <input type="text" class="form-control form-control-sm"
                                          required name="a_url" id="a_url">
                                  </div>
                                  <div class="col-md-4 mb-2">
                                      <label>User Name</label>
                                  </div>
                                  <div class="col-md-8 mb-2">
                                      <input type="text" class="form-control form-control-sm"
                                          required name="a_user_name" id="a_user_name">
                                  </div>
                                  <div class="col-md-4 mb-2">
                                      <label>Password</label>
                                  </div>
                                  <div class="col-md-8 mb-2">
                                      <input type="password" class="form-control form-control-sm"
                                          required name="a_pass" id="a_pass">
                                  </div>
                                  <div class="col-md-4 mb-2">
                                    <label>Security Questions</label>
                                </div>
                                <div class="col-md-8 mb-2">
                                    <input type="text" class="form-control form-control-sm"
                                        required name="a_question" id="a_question">
                                </div>
                                <div class="col-md-4 mb-2">
                                      <label>Answers</label>
                                  </div>
                                  <div class="col-md-8 mb-2">
                                      <input type="text" class="form-control form-control-sm"
                                          required name="a_ans" id="a_ans">
                                  </div>
                              </div>
                          </div>
                          <div class="modal-footer">
                              <button type="button" class="btn btn-primary" id="save_online_access">Save</button>
                              <button type="button" class="btn btn-danger"
                                  data-dismiss="modal">Close</button>
                          </div>
                      </form>
                  </div>
              </div>
            </div>

        </form>

    </div>
@endsection
@section('js')
    <script>
        $(document).ready(function(){
            var contract_view;
            function save_online_access(){
                $('#loading').show();
                $.ajax({
                    url: "{{route('provider.save.online.access.pro')}}",
                    method:"POST",
                    data:{
                      "_token" : "{{csrf_token()}}",
                      "a_name" : $('#a_name').val(),
                      "a_url" : $('#a_url').val(),
                      "a_user_name" : $('#a_user_name').val(),
                      "a_pass" : $('#a_pass').val(),
                      "a_question" : $('#a_question').val(),
                      "a_ans" : $('#a_ans').val(),
                    },
                    success:function(data){
                        if(data == "success"){
                            $('#loading').hide();
                            toastr["success"]("Saved successfully!",'ALERT!');
                            $('#addAccess').modal('hide');
                            fetch_online_access();
                        }
                    }
                });
            }


            $('#save_online_access').click(function(){
              save_online_access();
            })

            function fetch_contract_view(){
              $.ajax({
                  url:"{{route('provider.get.contract.view')}}",
                  method:"POST",
                  data:{
                    "_token" : "{{csrf_token()}}",
                  },
                  success:function(data){
                      contract_view = data.view;
                      $('#contract_section').html(data.old_view)
                  }
              });
            }

            fetch_contract_view();
            let check_validation = 1
            $('#next_1').click(function(){
                let pr_business_name =$('.pr_business_name').val();
                let pr_dba_name = $('.pr_dba_name').val();
                let pr_tax_id = $('.pr_tax_id').val();
                let pr_npi = $('.pr_npi').val();
                let pr_phone_number = $('.pr_phone_number').val();
                let pr_age_limit = $('.pr_age_limit').val();
                let pr_working_hrs = $('.pr_working_hrs').val();
                let pr_language_spoken = $('.pr_language_spoken').val();
                if(pr_business_name == ""){
                    toastr["error"]("Please enter business name!",'ALERT!');
                    check_validation = 0
                    return false;
                    if(pr_dba_name == ""){
                        toastr["error"]("Please enter DBA name!",'ALERT!');
                        check_validation = 0
                        return false;

                        if(pr_tax_id == ""){
                            toastr["error"]("Please enter tax id!",'ALERT!');
                            check_validation = 0
                            return false;

                            if(pr_npi == ""){
                                toastr["error"]("Please enter NPI!",'ALERT!');
                                check_validation = 0
                                return false;

                                if(pr_phone_number == ""){
                                    toastr["error"]("Please enter phone number!",'ALERT!');
                                    check_validation = 0
                                    return false;

                                    if(pr_age_limit == ""){
                                        toastr["error"]("Please enter age limit!",'ALERT!');
                                        check_validation = 0
                                        return false;

                                        if(pr_working_hrs == ""){
                                            toastr["error"]("Please enter working hours!",'ALERT!');
                                            check_validation = 0
                                            return false;

                                            if(pr_language_spoken == ""){
                                                toastr["error"]("Please enter language spoken!",'ALERT!');
                                                check_validation = 0
                                                return false;

                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
                check_validation = 1
                var form1 = document.getElementById('msform');
                var formData1 = new FormData(form1);
                $('#loading').show();
                $.ajax({
                    url:"{{route('provider.save.practice.info')}}",
                    method:"POST",
                    data:formData1,
                    cache : false,
                    processData: false,
                    contentType: false,
                    success:function(data){
                        $('#loading').hide();
                    }
                });
            })

            $('#add_sig1').click(function(){
                let canvas = document.getElementById('sig-canvas');
                let dataURL = canvas.toDataURL();
                $('.sign1').val(dataURL);
                $('#sig_img').attr('src',dataURL);
            })

            $('#add_sig2').click(function(){
                let canvas2 = document.getElementById('sig-canvas2');
                let dataURL2 = canvas2.toDataURL();
            })

            $('#next_2').click(function(){
                let first_name = $('.first_name').val();
                let last_name = $('.last_name').val();
                let dob = $('.dob').val();
                let speciality = $('.speciality').val();
                let tax_id = $('.tax_id').val();
                let ssn = $('.ssn').val();
                let npi = $('.npi').val();
                let upin = $('.upin').val();
                let dea = $('.dea').val();
                let state_licence = $('.state_licence').val();
                let phone = $('.phone').val();
                let email = $('.email').val();
                let start_date = $('.start_date').val();

                if(first_name == ""){
                    toastr["error"]("Please enter first name!",'ALERT!');
                    return false;
                    if(last_name == ""){
                        toastr["error"]("Please enter last name!",'ALERT!');
                        return false;
                        if(dob == ""){
                            toastr["error"]("Please enter date of birth!",'ALERT!');
                            return false;
                            if(speciality == ""){
                                toastr["error"]("Please enter speciality!",'ALERT!');
                                return false;
                                if(tax_id == ""){
                                    toastr["error"]("Please enter tax id!",'ALERT!');
                                    return false;
                                    if(ssn == ""){
                                        toastr["error"]("Please enter SSN!",'ALERT!');
                                        return false;
                                        if(npi == ""){
                                            toastr["error"]("Please enter NPI!",'ALERT!');
                                            return false;
                                            if(upin == ""){
                                                toastr["error"]("Please enter UPIN!",'ALERT!');
                                                return false;
                                                if(dea == ""){
                                                    toastr["error"]("Please enter DEA!",'ALERT!');
                                                    return false;
                                                    if(state_licence == ""){
                                                        toastr["error"]("Please enter state licence!",'ALERT!');
                                                        return false;
                                                        if(phone == ""){
                                                            toastr["error"]("Please enter phone number!",'ALERT!');
                                                            return false;
                                                            if(email == ""){
                                                                toastr["error"]("Please enter email!",'ALERT!');
                                                                return false;
                                                                if(start_date == ""){
                                                                    toastr["error"]("Please enter start date!",'ALERT!');
                                                                    return false;
                                                                }
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }

                var form2 = document.getElementById('msform');
                var formData2 = new FormData(form2);
                $('#loading').show();
                $.ajax({
                    url:"{{route('provider.save.info')}}",
                    method:"POST",
                    data:formData2,
                    cache : false,
                    processData: false,
                    contentType: false,
                    success:function(data){
                        $('#loading').hide();
                    }
                });


            })

            $('#next_3').click(function(){

                var form3 = document.getElementById('msform');
                var formData3 = new FormData(form3);
                $('#loading').show();
                $.ajax({
                    url:"{{route('provider.save.question')}}",
                    method:"POST",
                    data:formData3,
                    cache : false,
                    processData: false,
                    contentType: false,
                    success:function(data){
                        $('#loading').hide();
                        if(!(data == '' || data == null)){
                            url = "{{asset('/')}}"+data;
                            console.log(url);
                            $('#sig_img').attr("src",url);
                        }
                    }
                });


            })

            $('#next_4').click(function(){

                var form4 = document.getElementById('msform');
                var formData4 = new FormData(form4);
                $('#loading').show();
                $.ajax({
                    url:"{{route('provider.save.authorization')}}",
                    method:"POST",
                    data:formData4,
                    cache : false,
                    processData: false,
                    contentType: false,
                    success:function(data){
                        if(data == "success"){
                            $('#loading').hide();
                            toastr["success"]("Saved successfully!",'ALERT!');
                        }
                    }
                });

            })

            $('#next_5').click(function(){

                var form5 = document.getElementById('msform');
                var formData5 = new FormData(form5);
                $('#loading').show();
                $.ajax({
                    url:"{{route('provider.save.contract')}}",
                    method:"POST",
                    data:formData5,
                    cache : false,
                    processData: false,
                    contentType: false,
                    success:function(data){
                        if(data == "success"){
                            $('#loading').hide();
                            toastr["success"]("Saved successfully!",'ALERT!');
                        }
                    }
                });
            })

            $('#add_contract').click(function(){
              $('#new_contract_section').append(contract_view);
            })

            function fetch_online_access(){
              $.ajax({
                url:"{{route('provider.get.online.access')}}",
                method:"POST",
                data:{
                  "_token" : "{{csrf_token()}}",
                },
                success:function(data){
                  $('#online_table').html(data.view);
                }
              });
            }

            fetch_online_access();

            $('#add_sig1').click(function(){
              if($('.file1').get(0).files.length > 0){
                file = $('.file1').get(0).files[0];
                console.log('clicked',file)
                sig_preview(file);
              }
              else{

              }
            })

            function sig_preview(file){
              var reader = new FileReader();
              reader.onload = function(){
                  $("#sig_img").attr("src",reader.result);
              }
              reader.readAsDataURL(file);
            }

        })
    </script>



    <script>
      $(document).ready(function () {

        var current_fs, next_fs, previous_fs; //fieldsets
        var opacity;
        var current = 1;
        var steps = $("fieldset").length;

        setProgressBar(current);

        $(".next").click(function () {
            if(check_validation == 0){
                return false
            }
          current_fs = $(this).parent();
          next_fs = $(this).parent().next();

          //Add Class Active
          $("#progressbar li").eq($("fieldset").index(next_fs)).addClass("active");

          //show the next fieldset
          next_fs.show();
          //hide the current fieldset with style
          current_fs.animate({
            opacity: 0
          }, {
            step: function (now) {
              // for making fielset appear animation
              opacity = 1 - now;

              current_fs.css({
                'display': 'none',
                'position': 'relative'
              });
              next_fs.css({
                'opacity': opacity
              });
            },
            duration: 500
          });
          setProgressBar(++current);
        });

        $(".previous").click(function () {

          current_fs = $(this).parent();
          previous_fs = $(this).parent().prev();

          //Remove class active
          $("#progressbar li").eq($("fieldset").index(current_fs)).removeClass("active");

          //show the previous fieldset
          previous_fs.show();

          //hide the current fieldset with style
          current_fs.animate({
            opacity: 0
          }, {
            step: function (now) {
              // for making fielset appear animation
              opacity = 1 - now;

              current_fs.css({
                'display': 'none',
                'position': 'relative'
              });
              previous_fs.css({
                'opacity': opacity
              });
            },
            duration: 500
          });
          setProgressBar(--current);
        });

        function setProgressBar(curStep) {
          var percent = parseFloat(100 / steps) * curStep;
          percent = percent.toFixed();
          $(".progress-bar")
            .css("width", percent + "%")
        }

        $(".submit").click(function () {
          return false;
        })
    });
    </script>
    <script src="{{ asset('assets/provider/') }}/signature/sketchpad.js"></script>
    <script>

        $('#signatureModal').on('shown.bs.modal', function () {
            var modalDialogHeight = $(this).find('.modal-body').outerHeight(true);
            var modalDialogWidth = $(this).find('.modal-body').outerWidth(true);

            var sketchpad = new Sketchpad({
                element: '#sig-canvas',
                height: modalDialogHeight-190,
                width: modalDialogWidth-35
            });

            sketchpad.penSize = 3;
            $('#sig-clearBtn').click(function(){
                    sketchpad.clear();
            })
        });

        $('#signatureModal2').on('shown.bs.modal', function () {
            var modalDialogHeight = $(this).find('.modal-body').outerHeight(true);
            var modalDialogWidth = $(this).find('.modal-body').outerWidth(true);

            var sketchpad2 = new Sketchpad({
                element: '#sig-canvas2',
                height: modalDialogHeight-190,
                width: modalDialogWidth-35
            });

            sketchpad2.penSize = 3;
            $('#sig-clearBtn2').click(function(){
                    sketchpad2.clear();
            })
        });
        function isCanvasBlank(canvas) {
            const context = canvas.getContext('2d');

            const pixelBuffer = new Uint32Array(
                context.getImageData(0, 0, canvas.width, canvas.height).data.buffer
            );

            return !pixelBuffer.some(color => color !== 0);
        }
    </script>


    <script>

      $(document).on('change','.up_file', function(){

          previewFile($(this),$(this).data('id'), $(this).data("type"),'#upload_div');
      });

      $(document).on('change','.up_file2', function(){
          previewFile($(this),$(this).data('id'), $(this).data("type"),'#upload_div2',1);
      });



    function previewFile(selector,id, type, append_selector, provider_doc = 0){
        var files = selector.get(0).files;
        $.each(files, function(index,file){
          appendUploadDiv(append_selector,file,id,index,type, provider_doc);
        });
    }

    function appendUploadDiv(selector, file, id, index, type, provider_doc){
      fileName = file.name;
      extension = fileName.split('.').pop();
      $('.'+id+index).each(function(){
        $(this).remove();
      })

      $(selector).append(`
            <div class="col-md-12 `+id+index+`">
              <div class="upload_file_sec">
                <div class="upload_file_sec_content">
                  <table role="presentation" class="table table-striped">
                    <div class="files">
                      <ul class="template-upload fade in flex-div">
                        <li class="preview_image">
                          <span class="preview" id="file_preview`+id+index+`">

                          </span>
                        </li>
                        <li class="file_name">
                          <p class="name">`+fileName+`</p>
                          <strong class="error text-danger"></strong></li>
                        <li class="progressbar_sec">
                          <div class="progress">
                            <div class="progress-bar progress-bar-striped progress-bar-animated bar`+id+index+`" role="progressbar" style="width: 0%;" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100">0%</div>
                          </div>
                        </li>
                        <li class="right_btn">
                          <div class="btn_group">
                            <button type="button" class="btn btn-primary start m-t-10 start_upload" id="start_upload_btn`+id+index+`" data-check="`+id+`" data-index="`+index+`" data-type="`+type+`" data-prodoc = "`+provider_doc+`"> <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-upload" viewBox="0 0 16 16">
                            <path d="M.5 9.9a.5.5 0 0 1 .5.5v2.5a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1v-2.5a.5.5 0 0 1 1 0v2.5a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2v-2.5a.5.5 0 0 1 .5-.5z"></path>
                            <path d="M7.646 1.146a.5.5 0 0 1 .708 0l3 3a.5.5 0 0 1-.708.708L8.5 2.707V11.5a.5.5 0 0 1-1 0V2.707L5.354 4.854a.5.5 0 1 1-.708-.708l3-3z"></path>
                            </svg> <span>Start</span> </button>
                            <button type="button" class="btn btn-warning cancel m-t-10 cancel_upload" id="cancel_upload_btn`+id+index+`" data-id="`+id+index+`" data-prodoc = "`+provider_doc+`"> <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-slash-circle" viewBox="0 0 16 16">
                            <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"></path>
                            <path d="M11.354 4.646a.5.5 0 0 0-.708 0l-6 6a.5.5 0 0 0 .708.708l6-6a.5.5 0 0 0 0-.708z"></path>
                            </svg> <span>Cancel</span> </button>
                          </div>
                        </li>
                      </ul>
                    </div>
                  </table>
                </div>
              </div>
            </div>
        `).children(':last').hide().fadeIn(1000);
      if(extension == 'jpg' || extension == 'png' || extension == 'jpeg'){
        image_preview(file, id+index);
      }
      else{
        src = "{{asset('assets/dashboard/images/favicon.png')}}";
        $('#file_preview'+id+index).html('<img src="'+src+'">');
      }
    }

    function image_preview(file, id){
      var reader = new FileReader();
      reader.onload = function(){
          html = '<img src="'+reader.result+'">';
          $("#file_preview"+id).html(html);
      }
      reader.readAsDataURL(file);
    }

    $(document).on('click','.cancel_upload',function(){
      $('.'+$(this).data('id')).fadeOut(1000, function(){
        $('.'+$(this).data('id')).remove();
      });
    })

    function upload_file(selector, url, data){
      fd = new FormData();
      id = selector.data('check');
      index = selector.data('index');
      file_select = $("input[data-id='"+id+"']");
      u_file = file_select.get(0).files[index];
      fd.append('file',u_file);
      $.each(data, function(index,val){
        fd.append(index,val);
      });

      uploadAjax=$.ajax({
        headers: {'X-CSRF-TOKEN': '{{csrf_token()}}'},
        xhr: function() {
          var xhr = new window.XMLHttpRequest();
          xhr.upload.addEventListener("progress", function(evt) {
            $('#start_upload_btn'+id+index).prop('disabled',true);
            $('.bar'+id+index).removeClass('bg-danger');
            if (evt.lengthComputable) {
              var percentComplete = evt.loaded / evt.total;
              percentComplete = parseInt(percentComplete * 100);
              // console.log(percentComplete);
              $('.bar'+id+index).css("width", percentComplete+'%', function() {
                return $(this).attr("aria-valuenow", percentComplete) + "%";
              })

              $('.bar'+id+index).html(percentComplete+'%');

              if (percentComplete === 100) {

              }

            }
          }, false);

          return xhr;
        },
        url: url,
        type: "POST",
        data: fd,
        processData: false,
        contentType: false,
        cache: false,
        enctype: 'multipart/form-data',
        success: function(data) {
          if(data == "success"){
            selector.val(null);
          }
          else if(data == "not_found"){
            toastr["error"]("No Group Provider Found!","ALERT!");
            $('#start_upload_btn'+id+index).prop('disabled',false);
            $('.bar'+id+index).addClass('bg-danger');
          }
          else{
            toastr["error"]("Unexpected error occurred! Please try again later.","ALERT!");
            $('#start_upload_btn'+id+index).prop('disabled',false);
            $('.bar'+id+index).addClass('bg-danger');
          }
        },
        error: function(data) {
            $('#start_upload_btn'+id+index).prop('disabled',false);
            $('.bar'+id+index).addClass('bg-danger');
        }
      });
    }


    $(document).on('click','.start_upload', function(){
      upload_plugin($(this),'{{route('provider.practice.docs.save')}}');
    })

    $(document).on('click','.start_upload2', function(){

    })


      function upload_plugin(selector, url){
          upload_file(selector, url, {
            type : selector.data("type"),
            pro_id : "{{Auth::user()->id}}",
            pro_check : selector.data('prodoc'),
          });
      }
    </script>


  <script>
    $("#show-input-field").hide();
    $("#show-input").click(function (event){
      $("#show-input-field").show();
      $("#manage-space").hide();
    })
  </script>


@endsection
