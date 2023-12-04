``` gherkin
Given I am editing a <Method type> method's functions
And I am using <Automation> for automation
When I want to insert a new function between a(n) MF<Function pre> a(n) MF<Function post>
And I press the _Insert_ button
Then The <Insertable functions> MFs are available 
```


|Method type|Automation|Function pre|Function post|Insertable functions|
|-----------|:-----------:|-----------:|-----------:|-----------:|
|Bio Quant|CuvetteChanger|Blank|Measure (Blank)|Instruction, Wait, Aux value, Aux instrument|
|Bio Quant|CuvetteChanger|Calculation|Display results|Instruction, Wait, Aux value, Aux instrument, Report, Calculation|
|Bio Quant|CuvetteChanger|Calibration|Sample|Report, Aux instrument|
|Bio Quant|CuvetteChanger|Configuration|Blank|Instruction, Wait, Aux value, Aux instrument|
|Bio Quant|CuvetteChanger|Display results|Report|Instruction, Wait, Aux value, Aux instrument, Report, Calculation|
|Bio Quant|CuvetteChanger|Measure (Blank)|Standard|Instruction, Wait, Aux value, Aux instrument|
|Bio Quant|CuvetteChanger|Measure (Sample)|Calculation|Instruction, Wait, Aux value, Aux instrument, Report, Calculation|
|Bio Quant|CuvetteChanger|Measure (Standard)|Calibration|Instruction, Wait, Aux value, Aux instrument|
|Bio Quant|CuvetteChanger|Report|None|Instruction, Wait, Aux value, Aux instrument, Report, Calculation|
|Bio Quant|CuvetteChanger|Sample|Measure (Sample)|Instruction, Wait, Aux value, Aux instrument|
|Bio Quant|CuvetteChanger|Standard|Measure (Standard)|Instruction, Wait, Aux value, Aux instrument|
|Bio Quant|CuvetteChanger|Title|Configuration|Instruction, Wait, Aux value, Aux instrument|
|Bio Quant|FillPalMini|Blank|Fill|Instruction, Wait, Aux value, Aux instrument, Fill|
|Bio Quant|FillPalMini|Calculation|Display results|Instruction, Wait, Aux value, Aux instrument, Clean, Report|
|Bio Quant|FillPalMini|Calibration|Sample|Report, Aux instrument|
|Bio Quant|FillPalMini|Configuration|Blank|Instruction, Wait, Aux value, Aux instrument, Clean|
|Bio Quant|FillPalMini|Display results|Report|Instruction, Wait, Aux value, Aux instrument, Clean, Report, Calculation|
|Bio Quant|FillPalMini|Fill|Measure (Blank)|Instruction, Wait, Aux value, Aux instrument, Fill|
|Bio Quant|FillPalMini|Fill|Measure (Sample)|Instruction, Wait, Aux value, Aux instrument, Fill|
|Bio Quant|FillPalMini|Fill|Measure (Standard)|Instruction, Wait, Aux value, Aux instrument, Fill|
|Bio Quant|FillPalMini|Measure (Blank)|Standard|Instruction, Wait, Aux value, Aux instrument, Clean|
|Bio Quant|FillPalMini|Measure (Sample)|Calculation|Instruction, Wait, Aux value, Aux instrument, Clean, Report|
|Bio Quant|FillPalMini|Measure (Standard)|Calibration|Instruction, Wait, Aux value, Aux instrument, Clean|
|Bio Quant|FillPalMini|Report|None|Instruction, Wait, Aux value, Aux instrument, Clean, Report, Calculation|
|Bio Quant|FillPalMini|Sample|Fill|Instruction, Wait, Aux value, Aux instrument, Fill|
|Bio Quant|FillPalMini|Standard|Fill|Instruction, Wait, Aux value, Aux instrument, Fill|
|Bio Quant|FillPalMini|Title|Configuration|Instruction, Wait, Aux value, Aux instrument, Clean|
|Bio Quant|InMotion|Blank|Fill|Instruction, Wait, Aux value, Aux instrument, Fill, Stir, PowerShower|
|Bio Quant|InMotion|Calculation|Display results|Instruction, Wait, Aux value, Aux instrument, Clean, PowerShower, Report|
|Bio Quant|InMotion|Calibration|Sample|Report, Aux instrument|
|Bio Quant|InMotion|Configuration|Blank|Instruction, Wait, Aux value, Aux instrument, Clean|
|Bio Quant|InMotion|Display results|Report|Instruction, Wait, Aux value, Aux instrument, Clean, Report, Calculation, PowerShower|
|Bio Quant|InMotion|Fill|Measure (Blank)|Instruction, Wait, Aux value, Aux instrument, Fill, Stir, PowerShower|
|Bio Quant|InMotion|Fill|Measure (Sample)|Instruction, Wait, Aux value, Aux instrument, Fill, Stir, PowerShower|
|Bio Quant|InMotion|Fill|Measure (Standard)|Instruction, Wait, Aux value, Aux instrument, Fill, Stir, PowerShower|
|Bio Quant|InMotion|Measure (Blank)|Standard|Instruction, Wait, Aux value, Aux instrument, Clean, PowerShower|
|Bio Quant|InMotion|Measure (Sample)|Calculation|Instruction, Wait, Aux value, Aux instrument, Clean, Report, PowerShower|
|Bio Quant|InMotion|Measure (Standard)|Calibration|Instruction, Wait, Aux value, Aux instrument, Clean, PowerShower|
|Bio Quant|InMotion|Report|None|Instruction, Wait, Aux value, Aux instrument, Clean, Report, Calculation, PowerShower|
|Bio Quant|InMotion|Sample|Fill|Instruction, Wait, Aux value, Aux instrument, Fill, Stir, PowerShower|
|Bio Quant|InMotion|Standard|Fill|Instruction, Wait, Aux value, Aux instrument, Fill, Stir, PowerShower|
|Bio Quant|InMotion|Title|Configuration|Instruction, Wait, Aux value, Aux instrument, Clean|
|Bio Quant|None|Blank|Measure (Blank)|Instruction, Wait, Aux value, Aux instrument|
|Bio Quant|None|Calculation|Display results|Instruction, Wait, Aux value, Aux instrument, Report, Calculation|
|Bio Quant|None|Calibration|Sample|Report, Aux instrument|
|Bio Quant|None|Configuration|Blank|Instruction, Wait, Aux value, Aux instrument|
|Bio Quant|None|Display results|Report|Instruction, Wait, Aux value, Aux instrument, Report, Calculation|
|Bio Quant|None|Measure (Blank)|Standard|Instruction, Wait, Aux value, Aux instrument|
|Bio Quant|None|Measure (Sample)|Calculation|Instruction, Wait, Aux value, Aux instrument, Report, Calculation|
|Bio Quant|None|Measure (Standard)|Calibration|Instruction, Wait, Aux value, Aux instrument|
|Bio Quant|None|Report|None|Instruction, Wait, Aux value, Aux instrument, Report, Calculation|
|Bio Quant|None|Sample|Measure (Sample)|Instruction, Wait, Aux value, Aux instrument|
|Bio Quant|None|Standard|Measure (Standard)|Instruction, Wait, Aux value, Aux instrument|
|Bio Quant|None|Title|Configuration|Instruction, Wait, Aux value, Aux instrument|
|Bio fixed wavelength|CuvetteChanger|Blank|Measure (Blank)|Instruction, Wait, Aux value, Aux instrument|
|Bio fixed wavelength|CuvetteChanger|Calculation|Display results|Instruction, Wait, Aux value, Aux instrument, Report, Calculation|
|Bio fixed wavelength|CuvetteChanger|Configuration|Blank|Instruction, Wait, Aux value, Aux instrument|
|Bio fixed wavelength|CuvetteChanger|Display results|Report|Instruction, Wait, Aux value, Aux instrument, Report, Calculation|
|Bio fixed wavelength|CuvetteChanger|Measure (Blank)|Sample|Instruction, Wait, Aux value, Aux instrument|
|Bio fixed wavelength|CuvetteChanger|Measure (Sample)|Wavelength selection|Instruction, Wait, Aux value, Aux instrument|
|Bio fixed wavelength|CuvetteChanger|Report|None|Instruction, Wait, Aux value, Aux instrument, Report, Calculation|
|Bio fixed wavelength|CuvetteChanger|Sample|Measure (Sample)|Instruction, Wait, Aux value, Aux instrument|
|Bio fixed wavelength|CuvetteChanger|Title|Configuration|Instruction, Wait, Aux value, Aux instrument|
|Bio fixed wavelength|CuvetteChanger|Wavelength selection|Calculation|Instruction, Wait, Aux value, Aux instrument, Report, Calculation|
|Bio fixed wavelength|FillPalMini|Blank|Fill|Instruction, Wait, Aux value, Aux instrument, Fill|
|Bio fixed wavelength|FillPalMini|Calculation|Display results|Instruction, Wait, Aux value, Aux instrument, Report, Calculation, Clean|
|Bio fixed wavelength|FillPalMini|Configuration|Blank|Instruction, Wait, Aux value, Aux instrument, Clean|
|Bio fixed wavelength|FillPalMini|Display results|Report|Instruction, Wait, Aux value, Aux instrument, Report, Calculation, Clean|
|Bio fixed wavelength|FillPalMini|Fill|Measure (Blank)|Instruction, Wait, Aux value, Fill, Aux instrument|
|Bio fixed wavelength|FillPalMini|Fill|Measure (Sample)|Instruction, Wait, Aux value, Aux instrument, Fill|
|Bio fixed wavelength|FillPalMini|Measure (Blank)|Sample|Instruction, Wait, Aux value, Aux instrument, Clean|
|Bio fixed wavelength|FillPalMini|Measure (Sample)|Wavelength selection|Instruction, Wait, Aux value, Aux instrument, Clean|
|Bio fixed wavelength|FillPalMini|Report|None|Instruction, Wait, Aux value, Aux instrument, Report, Calculation, Clean|
|Bio fixed wavelength|FillPalMini|Sample|Fill|Instruction, Wait, Aux value, Fill, Aux instrument|
|Bio fixed wavelength|FillPalMini|Title|Configuration|Instruction, Wait, Aux value, Aux instrument|
|Bio fixed wavelength|FillPalMini|Wavelength selection|Calculation|Instruction, Wait, Aux value, Aux instrument, Report, Calculation, Clean|
|Bio fixed wavelength|InMotion|Blank|Fill|Instruction, Wait, Aux value, Aux instrument, Fill, Stir, PowerShower|
|Bio fixed wavelength|InMotion|Calculation|Display results|Instruction, Wait, Aux value, Aux instrument, Report, Calculation, Clean, PowerShower|
|Bio fixed wavelength|InMotion|Configuration|Blank|Instruction, Wait, Aux value, Aux instrument, Clean|
|Bio fixed wavelength|InMotion|Display results|Report|Instruction, Wait, Aux value, Aux instrument, Report, Calculation, Clean, PowerShower|
|Bio fixed wavelength|InMotion|Fill|Measure (Blank)|Instruction, Wait, Aux value, Aux instrument, Fill, Stir, PowerShower|
|Bio fixed wavelength|InMotion|Fill|Measure (Sample)|Instruction, Wait, Aux value, Aux instrument, Fill, Stir, PowerShower|
|Bio fixed wavelength|InMotion|Measure (Blank)|Sample|Instruction, Wait, Aux value, Aux instrument, Clean, PowerShower|
|Bio fixed wavelength|InMotion|Measure (Sample)|Wavelength selection|Instruction, Wait, Aux value, Aux instrument, Clean, PowerShower|
|Bio fixed wavelength|InMotion|Report|None|Instruction, Wait, Aux value, Aux instrument, Report, Calculation, Clean, PowerShower|
|Bio fixed wavelength|InMotion|Sample|Fill|Instruction, Wait, Aux value, Aux instrument, Fill, Stir, PowerShower|
|Bio fixed wavelength|InMotion|Title|Configuration|Instruction, Wait, Aux value, Aux instrument, Clean|
|Bio fixed wavelength|InMotion|Wavelength selection|Calculation|Instruction, Wait, Aux value, Aux instrument, Report, Calculation, Clean, PowerShower|
|Bio fixed wavelength|None|Blank|Measure (Blank)|Instruction, Wait, Aux value, Aux instrument|
|Bio fixed wavelength|None|Calculation|Display results|Instruction, Wait, Aux value, Aux instrument, Report, Calculation|
|Bio fixed wavelength|None|Configuration|Blank|Instruction, Wait, Aux value, Aux instrument|
|Bio fixed wavelength|None|Display results|Report|Instruction, Wait, Aux value, Aux instrument, Report, Calculation|
|Bio fixed wavelength|None|Measure (Blank)|Sample|Instruction, Wait, Aux value, Aux instrument|
|Bio fixed wavelength|None|Measure (Sample)|Wavelength selection|Instruction, Wait, Aux value, Aux instrument|
|Bio fixed wavelength|None|Report|None|Instruction, Wait, Aux value, Aux instrument, Report, Calculation|
|Bio fixed wavelength|None|Sample|Measure (Sample)|Instruction, Wait, Aux value, Aux instrument|
|Bio fixed wavelength|None|Title|Configuration|Instruction, Wait, Aux value, Aux instrument|
|Bio fixed wavelength|None|Wavelength selection|Calculation|Instruction, Wait, Aux value, Aux instrument, Report, Calculation|
|Fixed wavelength|CuvetteChanger|Blank|Measure (Blank)|Instruction, Wait, Aux value, Aux instrument|
|Fixed wavelength|CuvetteChanger|Calculation|Display results|Instruction, Wait, Aux value, Aux instrument, Report, Calculation|
|Fixed wavelength|CuvetteChanger|Configuration|Blank|Instruction, Wait, Aux value, Aux instrument|
|Fixed wavelength|CuvetteChanger|Display results|Report|Instruction, Wait, Aux value, Aux instrument, Report, Calculation|
|Fixed wavelength|CuvetteChanger|Measure (Blank)|Sample|Instruction, Wait, Aux value, Aux instrument|
|Fixed wavelength|CuvetteChanger|Measure (Sample)|Wavelength selection|Instruction, Wait, Aux value, Aux instrument|
|Fixed wavelength|CuvetteChanger|Report|None|Instruction, Wait, Aux value, Aux instrument, Report, Calculation|
|Fixed wavelength|CuvetteChanger|Sample|Measure (Sample)|Instruction, Wait, Aux value, Aux instrument|
|Fixed wavelength|CuvetteChanger|Title|Configuration|Instruction, Wait, Aux value, Aux instrument|
|Fixed wavelength|CuvetteChanger|Wavelength selection|Calculation|Instruction, Wait, Aux value, Aux instrument, Report, Calculation|
|Fixed wavelength|FillPalMini|Blank|Fill|Instruction, Wait, Aux value, Aux instrument, Fill|
|Fixed wavelength|FillPalMini|Calculation|Display results|Instruction, Wait, Aux value, Aux instrument, Report, Calculation, Clean|
|Fixed wavelength|FillPalMini|Configuration|Blank|Instruction, Wait, Aux value, Aux instrument, Clean|
|Fixed wavelength|FillPalMini|Display results|Report|Instruction, Wait, Aux value, Aux instrument, Report, Calculation, Clean|
|Fixed wavelength|FillPalMini|Fill|Measure (Blank)|Instruction, Wait, Aux value, Fill, Aux instrument|
|Fixed wavelength|FillPalMini|Fill|Measure (Sample)|Instruction, Wait, Aux value, Aux instrument, Fill|
|Fixed wavelength|FillPalMini|Measure (Blank)|Sample|Instruction, Wait, Aux value, Aux instrument, Clean|
|Fixed wavelength|FillPalMini|Measure (Sample)|Wavelength selection|Instruction, Wait, Aux value, Aux instrument, Clean|
|Fixed wavelength|FillPalMini|Report|None|Instruction, Wait, Aux value, Aux instrument, Report, Calculation, Clean|
|Fixed wavelength|FillPalMini|Sample|Fill|Instruction, Wait, Aux value, Fill, Aux instrument|
|Fixed wavelength|FillPalMini|Title|Configuration|Instruction, Wait, Aux value, Aux instrument|
|Fixed wavelength|FillPalMini|Wavelength selection|Calculation|Instruction, Wait, Aux value, Aux instrument, Report, Calculation, Clean|
|Fixed wavelength|InMotion|Blank|Fill|Instruction, Wait, Aux value, Aux instrument, Fill, Stir, PowerShower|
|Fixed wavelength|InMotion|Calculation|Display results|Instruction, Wait, Aux value, Aux instrument, Report, Calculation, Clean, PowerShower|
|Fixed wavelength|InMotion|Configuration|Blank|Instruction, Wait, Aux value, Aux instrument, Clean|
|Fixed wavelength|InMotion|Display results|Report|Instruction, Wait, Aux value, Aux instrument, Report, Calculation, Clean, PowerShower|
|Fixed wavelength|InMotion|Fill|Measure (Blank)|Instruction, Wait, Aux value, Aux instrument, Fill, Stir, PowerShower|
|Fixed wavelength|InMotion|Fill|Measure (Sample)|Instruction, Wait, Aux value, Aux instrument, Fill, Stir, PowerShower|
|Fixed wavelength|InMotion|Measure (Blank)|Sample|Instruction, Wait, Aux value, Aux instrument, Clean, PowerShower|
|Fixed wavelength|InMotion|Measure (Sample)|Wavelength selection|Instruction, Wait, Aux value, Aux instrument, Clean, PowerShower|
|Fixed wavelength|InMotion|Report|None|Instruction, Wait, Aux value, Aux instrument, Report, Calculation, Clean, PowerShower|
|Fixed wavelength|InMotion|Sample|Fill|Instruction, Wait, Aux value, Aux instrument, Fill, Stir, PowerShower|
|Fixed wavelength|InMotion|Title|Configuration|Instruction, Wait, Aux value, Aux instrument, Clean|
|Fixed wavelength|InMotion|Wavelength selection|Calculation|Instruction, Wait, Aux value, Aux instrument, Report, Calculation, Clean, PowerShower|
|Fixed wavelength|None|Blank|Measure (Blank)|Instruction, Wait, Aux value, Aux instrument|
|Fixed wavelength|None|Calculation|Display results|Instruction, Wait, Aux value, Aux instrument, Report, Calculation|
|Fixed wavelength|None|Configuration|Blank|Instruction, Wait, Aux value, Aux instrument|
|Fixed wavelength|None|Display results|Report|Instruction, Wait, Aux value, Aux instrument, Report, Calculation|
|Fixed wavelength|None|Measure (Blank)|Sample|Instruction, Wait, Aux value, Aux instrument|
|Fixed wavelength|None|Measure (Sample)|Wavelength selection|Instruction, Wait, Aux value, Aux instrument|
|Fixed wavelength|None|Report|None|Instruction, Wait, Aux value, Aux instrument, Report, Calculation|
|Fixed wavelength|None|Sample|Measure (Sample)|Instruction, Wait, Aux value, Aux instrument|
|Fixed wavelength|None|Title|Configuration|Instruction, Wait, Aux value, Aux instrument|
|Fixed wavelength|None|Wavelength selection|Calculation|Instruction, Wait, Aux value, Aux instrument, Report, Calculation|
|Kinetics|CuvetteChanger|Blank|Measure (Blank)|None|
|Kinetics|CuvetteChanger|Configuration|Blank|Instruction, Wait, Aux value, Aux instrument|
|Kinetics|CuvetteChanger|Display results|Report|Instruction, Wait, Aux value, Aux instrument, Report, Calculation|
|Kinetics|CuvetteChanger|Kinetics|Display results|Aux value, Report, Calculation|
|Kinetics|CuvetteChanger|Measure (Blank)|Sample|None|
|Kinetics|CuvetteChanger|Measure (Sample)|Kinetics|None|
|Kinetics|CuvetteChanger|Report|None|Instruction, Wait, Aux value, Aux instrument, Report, Calculation|
|Kinetics|CuvetteChanger|Sample|Measure (Sample)|None|
|Kinetics|CuvetteChanger|Title|Configuration|Instruction, Wait, Aux value, Aux instrument|
|Kinetics|FillPalMini|Blank|Fill|Instruction, Wait, Aux value, Aux instrument, Fill|
|Kinetics|FillPalMini|Configuration|Blank|Instruction, Wait, Aux value, Aux instrument, Clean|
|Kinetics|FillPalMini|Display results|Report|Instruction, Wait, Aux value, Aux instrument, Report, Calculation, Clean|
|Kinetics|FillPalMini|Fill|Measure (Blank)|Instruction, Wait, Aux value, Aux instrument, Fill|
|Kinetics|FillPalMini|Fill|Measure (Sample)|Aux instrument, Fill|
|Kinetics|FillPalMini|Kinetics|Display results|Aux value, Aux instrument, Report, Calculation, Clean|
|Kinetics|FillPalMini|Measure (Blank)|Sample|Instruction, Wait, Aux value, Aux instrument, Clean|
|Kinetics|FillPalMini|Measure (Sample)|Kinetics|None|
|Kinetics|FillPalMini|Report|None|Instruction, Wait, Aux value, Aux instrument, Report, Calculation, Clean|
|Kinetics|FillPalMini|Sample|Fill|Aux instrument, Fill|
|Kinetics|FillPalMini|Title|Configuration|Instruction, Wait, Aux value, Aux instrument|
|Kinetics|InMotion|Blank|Fill|Instruction, Wait, Aux value, Aux instrument, Fill, Stir, PowerShower|
|Kinetics|InMotion|Configuration|Blank|Instruction, Wait, Aux value, Aux instrument, Clean|
|Kinetics|InMotion|Display results|Report|Instruction, Wait, Aux value, Aux instrument, Report, Calculation, Clean, PowerShower|
|Kinetics|InMotion|Fill|Measure (Blank)|Instruction, Wait, Aux value, Aux instrument, Fill, Stir, PowerShower|
|Kinetics|InMotion|Fill|Measure (Sample)|Aux instrument, Fill, Stir, PowerShower|
|Kinetics|InMotion|Kinetics|Display results|Aux value, Aux instrument, Report, Calculation, Clean, PowerShower|
|Kinetics|InMotion|Measure (Blank)|Sample|Instruction, Wait, Aux value, Aux instrument, Clean, PowerShower|
|Kinetics|InMotion|Measure (Sample)|Kinetics|None|
|Kinetics|InMotion|Report|None|Instruction, Wait, Aux value, Aux instrument, Report, Calculation, Clean, PowerShower|
|Kinetics|InMotion|Sample|Fill|Aux instrument, Fill, Stir, PowerShower|
|Kinetics|InMotion|Title|Configuration|Instruction, Wait, Aux value, Aux instrument, Clean|
|Kinetics|None|Blank|Measure (Blank)|Instruction, Wait, Aux value, Aux instrument|
|Kinetics|None|Configuration|Blank|Instruction, Wait, Aux value, Aux instrument|
|Kinetics|None|Display results|Report|Instruction, Wait, Aux value, Aux instrument, Report, Calculation|
|Kinetics|None|Kinetics|Display results|Aux value, Aux instrument, Report, Calculation|
|Kinetics|None|Measure (Blank)|Sample|Instruction, Wait, Aux value, Aux instrument|
|Kinetics|None|Measure (Sample)|Kinetics|None|
|Kinetics|None|Report|None|Instruction, Wait, Aux value, Aux instrument, Report, Calculation|
|Kinetics|None|Sample|Measure (Sample)|Aux instrument|
|Kinetics|None|Title|Configuration|Instruction, Wait, Aux value, Aux instrument|
|Quant|CuvetteChanger|Blank|Measure (Blank)|Instruction, Wait, Aux value, Aux instrument|
|Quant|CuvetteChanger|Calculation|Display results|Instruction, Wait, Aux value, Aux instrument, Report, Calculation|
|Quant|CuvetteChanger|Calibration|Sample|Report, Aux instrument|
|Quant|CuvetteChanger|Configuration|Blank|Instruction, Wait, Aux value, Aux instrument|
|Quant|CuvetteChanger|Display results|Report|Instruction, Wait, Aux value, Aux instrument, Report, Calculation|
|Quant|CuvetteChanger|Measure (Blank)|Standard|Instruction, Wait, Aux value, Aux instrument|
|Quant|CuvetteChanger|Measure (Sample)|Calculation|Instruction, Wait, Aux value, Aux instrument, Report, Calculation|
|Quant|CuvetteChanger|Measure (Standard)|Calibration|Instruction, Wait, Aux value, Aux instrument|
|Quant|CuvetteChanger|Report|None|Instruction, Wait, Aux value, Aux instrument, Report, Calculation|
|Quant|CuvetteChanger|Sample|Measure (Sample)|Instruction, Wait, Aux value, Aux instrument|
|Quant|CuvetteChanger|Standard|Measure (Standard)|Instruction, Wait, Aux value, Aux instrument|
|Quant|CuvetteChanger|Title|Configuration|Instruction, Wait, Aux value, Aux instrument|
|Quant|FillPalMini|Blank|Fill|Instruction, Wait, Aux value, Aux instrument, Fill|
|Quant|FillPalMini|Calculation|Display results|Instruction, Wait, Aux value, Aux instrument, Clean, Report|
|Quant|FillPalMini|Calibration|Sample|Report, Aux instrument|
|Quant|FillPalMini|Configuration|Blank|Instruction, Wait, Aux value, Aux instrument, Clean|
|Quant|FillPalMini|Display results|Report|Instruction, Wait, Aux value, Aux instrument, Clean, Report, Calculation|
|Quant|FillPalMini|Fill|Measure (Blank)|Instruction, Wait, Aux value, Aux instrument, Fill|
|Quant|FillPalMini|Fill|Measure (Sample)|Instruction, Wait, Aux value, Aux instrument, Fill|
|Quant|FillPalMini|Fill|Measure (Standard)|Instruction, Wait, Aux value, Aux instrument, Fill|
|Quant|FillPalMini|Measure (Blank)|Standard|Instruction, Wait, Aux value, Aux instrument, Clean|
|Quant|FillPalMini|Measure (Sample)|Calculation|Instruction, Wait, Aux value, Aux instrument, Clean, Report|
|Quant|FillPalMini|Measure (Standard)|Calibration|Instruction, Wait, Aux value, Aux instrument, Clean|
|Quant|FillPalMini|Report|None|Instruction, Wait, Aux value, Aux instrument, Clean, Report, Calculation|
|Quant|FillPalMini|Sample|Fill|Instruction, Wait, Aux value, Aux instrument, Fill|
|Quant|FillPalMini|Standard|Fill|Instruction, Wait, Aux value, Aux instrument, Fill|
|Quant|FillPalMini|Title|Configuration|Instruction, Wait, Aux value, Aux instrument, Clean|
|Quant|InMotion|Blank|Fill|Instruction, Wait, Aux value, Aux instrument, Fill, Stir, PowerShower|
|Quant|InMotion|Calculation|Display results|Instruction, Wait, Aux value, Aux instrument, Clean, PowerShower, Report|
|Quant|InMotion|Calibration|Sample|Report, Aux instrument|
|Quant|InMotion|Configuration|Blank|Instruction, Wait, Aux value, Aux instrument, Clean|
|Quant|InMotion|Display results|Report|Instruction, Wait, Aux value, Aux instrument, Clean, Report, Calculation, PowerShower|
|Quant|InMotion|Fill|Measure (Blank)|Instruction, Wait, Aux value, Aux instrument, Fill, Stir, PowerShower|
|Quant|InMotion|Fill|Measure (Sample)|Instruction, Wait, Aux value, Aux instrument, Fill, Stir, PowerShower|
|Quant|InMotion|Fill|Measure (Standard)|Instruction, Wait, Aux value, Aux instrument, Fill, Stir, PowerShower|
|Quant|InMotion|Measure (Blank)|Standard|Instruction, Wait, Aux value, Aux instrument, Clean, PowerShower|
|Quant|InMotion|Measure (Sample)|Calculation|Instruction, Wait, Aux value, Aux instrument, Clean, Report, PowerShower|
|Quant|InMotion|Measure (Standard)|Calibration|Instruction, Wait, Aux value, Aux instrument, Clean, PowerShower|
|Quant|InMotion|Report|None|Instruction, Wait, Aux value, Aux instrument, Clean, Report, Calculation, PowerShower|
|Quant|InMotion|Sample|Fill|Instruction, Wait, Aux value, Aux instrument, Fill, Stir, PowerShower|
|Quant|InMotion|Standard|Fill|Instruction, Wait, Aux value, Aux instrument, Fill, Stir, PowerShower|
|Quant|InMotion|Title|Configuration|Instruction, Wait, Aux value, Aux instrument, Clean|
|Quant|None|Blank|Measure (Blank)|Instruction, Wait, Aux value, Aux instrument|
|Quant|None|Calculation|Display results|Instruction, Wait, Aux value, Aux instrument, Report, Calculation|
|Quant|None|Calibration|Sample|Report, Aux instrument|
|Quant|None|Configuration|Blank|Instruction, Wait, Aux value, Aux instrument|
|Quant|None|Display results|Report|Instruction, Wait, Aux value, Aux instrument, Report, Calculation|
|Quant|None|Measure (Blank)|Standard|Instruction, Wait, Aux value, Aux instrument|
|Quant|None|Measure (Sample)|Calculation|Instruction, Wait, Aux value, Aux instrument, Report, Calculation|
|Quant|None|Measure (Standard)|Calibration|Instruction, Wait, Aux value, Aux instrument|
|Quant|None|Report|None|Instruction, Wait, Aux value, Aux instrument, Report, Calculation|
|Quant|None|Sample|Measure (Sample)|Instruction, Wait, Aux value, Aux instrument|
|Quant|None|Standard|Measure (Standard)|Instruction, Wait, Aux value, Aux instrument|
|Quant|None|Title|Configuration|Instruction, Wait, Aux value, Aux instrument|
|Scanning|CuvetteChanger|Blank|Measure (Blank)|Instruction, Wait, Aux value, Aux instrument|
|Scanning|CuvetteChanger|Configuration|Blank|Instruction, Wait, Aux value, Aux instrument|
|Scanning|CuvetteChanger|Display results|Report|Instruction, Wait, Aux value, Aux instrument, Report, Calculation|
|Scanning|CuvetteChanger|Measure (Blank)|Sample|Instruction, Wait, Aux value, Aux instrument|
|Scanning|CuvetteChanger|Measure (Sample)|Spectrum evaluation|Instruction, Wait, Aux value, Aux instrument|
|Scanning|CuvetteChanger|Report|None|Instruction, Wait, Aux value, Aux instrument, Report, Calculation|
|Scanning|CuvetteChanger|Sample|Measure (Sample)|Instruction, Wait, Aux value, Aux instrument|
|Scanning|CuvetteChanger|Spectrum evaluation|Display results|Instruction, Wait, Aux value, Aux instrument, Report, Calculation|
|Scanning|CuvetteChanger|Title|Configuration|Instruction, Wait, Aux value, Aux instrument|
|Scanning|FillPalMini|Blank|Fill|Instruction, Wait, Aux value, Aux instrument, Fill|
|Scanning|FillPalMini|Configuration|Blank|Instruction, Wait, Aux value, Aux instrument, Clean|
|Scanning|FillPalMini|Display results|Report|Instruction, Wait, Aux value, Aux instrument, Report, Calculation, Clean|
|Scanning|FillPalMini|Fill|Measure (Blank)|Instruction, Wait, Aux value, Aux instrument, Fill|
|Scanning|FillPalMini|Fill|Measure (Sample)|Instruction, Wait, Aux value, Fill, Aux instrument|
|Scanning|FillPalMini|Measure (Blank)|Sample|Instruction, Wait, Aux value, Aux instrument, Clean|
|Scanning|FillPalMini|Measure (Sample)|Spectrum evaluation|Instruction, Wait, Aux value, Aux instrument, Clean|
|Scanning|FillPalMini|Report|None|Instruction, Wait, Aux value, Aux instrument, Report, Calculation, Clean|
|Scanning|FillPalMini|Sample|Fill|Instruction, Wait, Aux value, Aux instrument, Fill|
|Scanning|FillPalMini|Spectrum evaluation|Display results|Instruction, Wait, Aux value, Aux instrument, Report, Calculation, Clean|
|Scanning|FillPalMini|Title|Configuration|Instruction, Wait, Aux value, Aux instrument|
|Scanning|InMotion|Blank|Fill|Instruction, Wait, Aux value, Aux instrument, Fill, Stir, PowerShower|
|Scanning|InMotion|Configuration|Blank|Instruction, Wait, Aux value, Aux instrument, Clean|
|Scanning|InMotion|Display results|Report|Instruction, Wait, Aux value, Aux instrument, Report, Calculation, Clean, PowerShower|
|Scanning|InMotion|Fill|Measure (Blank)|Instruction, Wait, Aux value, Aux instrument, Fill, Stir, PowerShower|
|Scanning|InMotion|Fill|Measure (Sample)|Instruction, Wait, Aux value, Aux instrument, Fill, Stir, PowerShower|
|Scanning|InMotion|Measure (Blank)|Sample|Instruction, Wait, Aux value, Aux instrument, Clean, PowerShower|
|Scanning|InMotion|Measure (Sample)|Spectrum evaluation|Instruction, Wait, Aux value, Aux instrument, Clean, PowerShower|
|Scanning|InMotion|Report|None|Instruction, Wait, Aux value, Aux instrument, Report, Calculation, Clean, PowerShower|
|Scanning|InMotion|Sample|Fill|Instruction, Wait, Aux value, Aux instrument, Fill, Stir, PowerShower|
|Scanning|InMotion|Spectrum evaluation|Display results|Instruction, Wait, Aux value, Aux instrument, Report, Calculation, Clean, PowerShower|
|Scanning|InMotion|Title|Configuration|Instruction, Wait, Aux value, Aux instrument, Clean|
|Scanning|None|Blank|Measure (Blank)|Instruction, Wait, Aux value, Aux instrument|
|Scanning|None|Configuration|Blank|Instruction, Wait, Aux value, Aux instrument|
|Scanning|None|Display results|Report|Instruction, Wait, Aux value, Aux instrument, Report, Calculation|
|Scanning|None|Measure (Blank)|Sample|Instruction, Wait, Aux value, Aux instrument|
|Scanning|None|Measure (Sample)|Spectrum evaluation|Instruction, Wait, Aux value, Aux instrument|
|Scanning|None|Report|None|Instruction, Wait, Aux value, Aux instrument, Report, Calculation|
|Scanning|None|Sample|Measure (Sample)|Instruction, Wait, Aux value, Aux instrument|
|Scanning|None|Spectrum evaluation|Display results|Instruction, Wait, Aux value, Aux instrument, Report, Calculation|
|Scanning|None|Title|Configuration|Instruction, Wait, Aux value, Aux instrument|