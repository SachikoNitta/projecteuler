with Ada.Text_IO; use Ada.Text_IO;
with Ada.Integer_Text_IO; use Ada.Integer_Text_IO;

procedure Module_6 is
   Sum1  : Integer := 0;
   Sum2  : Integer := 0;
   Result1 : Integer;
   Result2 : Integer;
   Result  : Integer;
begin
   -- 和の二乗
   for I in 1 .. 100 loop
      Sum1 := Sum1 + I;
   end loop;
   Result1 := Sum1 * Sum1;

   -- 二乗の和
   for I in 1 .. 100 loop
      Sum2 := Sum2 + I * I;
   end loop;
   Result2 := Sum2;

   -- (和の二乗) - (二乗の和)
   Result := Result1 - Result2;

   Put(Result);
end Module_6;