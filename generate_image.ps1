Add-Type -AssemblyName System.Drawing

$width = 900
$height = 1200
$bmp = New-Object System.Drawing.Bitmap($width, $height)
$g = [System.Drawing.Graphics]::FromImage($bmp)
$g.Clear([System.Drawing.Color]::White)

$fontTitle = New-Object System.Drawing.Font('Arial', 24, [System.Drawing.FontStyle]::Bold)
$fontText = New-Object System.Drawing.Font('Arial', 18, [System.Drawing.FontStyle]::Regular)
$brushBlack = [System.Drawing.Brushes]::Black
$penGray = New-Object System.Drawing.Pen([System.Drawing.Color]::LightGray, 2)

$g.DrawString('DAVETLI MASA LISTESI', $fontTitle, $brushBlack, 220, 50)
$g.DrawLine($penGray, 50, 105, 850, 105)

$guests = @(
    'Kerem Yilmaz - Masa 12',
    'Selin Aksoy - Masa 5',
    'Tarkan Tevetoglu - Masa 1',
    'Beren Saat - Masa 8',
    'Kivanc Tatlitug - Masa 8',
    'Asli Enver - Masa 14',
    'Serkan Cayoglu - Masa 14',
    'Eda Ece - Masa 21',
    'Baris Arduc - Masa 3',
    'Elcin Sangu - Masa 3',
    'Engin Akyurek - Masa 7',
    'Demet Ozdemir - Masa 9'
)

$y = 140
foreach ($guest in $guests) {
    $g.DrawString($guest, $fontText, $brushBlack, 100, $y)
    $g.DrawLine($penGray, 80, ($y + 45), 820, ($y + 45))
    $y += 65
}

$outputPath = 'C:\Users\cydnr\Desktop\guester\test_yeni_kagit.png'
$bmp.Save($outputPath, [System.Drawing.Imaging.ImageFormat]::Png)
$g.Dispose()
$bmp.Dispose()
Write-Host "Başarıyla görsel üretildi: $outputPath"
