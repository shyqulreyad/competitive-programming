@if($count > 0)
  <div class="col-12 table-responsive">
    <table class="table table-sm table-bordered c_table">
      <thead>
        <tr>
          <th>Question</th>
          <th>Answer</th>
        </tr>
      </thead>
      <tbody>
        @foreach($questions as $q)
          <tr>
            <td>{{$q->questionData->question}}</td>
            <td>
                <input type="hidden" name="question_id[]" value="{{$q->questionData->id}}">
                <input type="hidden" name="question_type[]" value="{{$q->questionData->question_type}}">
                @if ($q->questionData->question_type == 1)
                  <textarea name="answer[]" id="" cols="30" rows="3"></textarea>
                @endif
                @if ($q->questionData->question_type == 2)
                  <input type="text" name="answer[]" class="form-control">
                @endif
                @if ($q->questionData->question_type == 3)
                <div class="col-md-12  ">
                   <div class="d-flex justify-content-between align-items-center">
                    <div class="mr-2 mb-2" style="width: 25%">
                        <button type="button" class="btn btn-sm btn-danger"  id="subtractButton"><i class="ri-subtract-line"></i></button>
                      </div>
                      <div class="mb-2" style="width: 40%">
                        <input class="form-control form-control-sm text-center" type="number" name="answer[]" id="count_input">
                      </div>
                      <div class="mr-2 mb-2" style="width: 25%">
                        <button type="button" class="btn btn-sm btn-primary"  id="addButton"><i class="ri-add-line"></i></button>
                      </div>
                   </div>
                </div>
                @endif
                @if ($q->questionData->question_type == 4)
                  <input type="time" class="form-control" name="answer[]">
                @endif
                @if ($q->questionData->question_type == 5)
                  <select name="answer[]" id="" class="form-control">
                    <option value="1">Select</option>
                    <option value="2">Select</option>
                    <option value="3">Select</option>
                  </select>
                @endif
            </td>
          </tr>
        @endforeach
      </tbody>
    </table>
  </div>
@else
  <div class="col-12">
    <div class="alert alert-danger"><b>INFO!</b> &nbsp No Tags available.</div>
  </div>
@endif
