; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

[Setup]
; NOTE: The value of AppId uniquely identifies this application. Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{8C273F29-5012-4F2E-8241-2A9EF5E4E9DB}
AppName=Computational Thematic Anlaysis Toolkit
AppVersion=0.8.5
AppPublisher=Robert P Gauthier
AppPublisherURL=https://github.com/rpgauthier/ComputationalThematicAnalysisToolkit
AppSupportURL=https://github.com/rpgauthier/ComputationalThematicAnalysisToolkit
AppUpdatesURL=https://github.com/rpgauthier/ComputationalThematicAnalysisToolkit
DefaultDirName={autopf}\Computational Thematic Anlaysis Toolkit
DisableProgramGroupPage=yes
LicenseFile={#SourcePath}\LICENSE
; Remove the following line to run in administrative install mode (install for all users.)
PrivilegesRequired=lowest
PrivilegesRequiredOverridesAllowed=dialog
OutputBaseFilename=ComputationalThematicAnalysisToolkit_Windows10x64
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Dirs]
Name: "{app}\bin"

[Files]
Source: "dist\bin\*"; DestDir: "{app}\bin"; Flags: ignoreversion recursesubdirs createallsubdirs
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{autoprograms}\Computational Thematic Anlaysis Toolkit"; Filename: "{app}\bin\Toolkit.exe"
Name: "{autodesktop}\Computational Thematic Anlaysis Toolkit"; Filename: "{app}\bin\Toolkit.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\bin\Toolkit.exe"; Description: "{cm:LaunchProgram,Computational Thematic Anlaysis Toolkit}"; Flags: nowait postinstall skipifsilent

