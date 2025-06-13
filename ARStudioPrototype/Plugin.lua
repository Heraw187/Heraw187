-- Plugin.lua: Connects to local AR server and updates Roblox objects
local HttpService = game:GetService("HttpService")
local RunService = game:GetService("RunService")

local ARServerUrl = "http://localhost:5000/tracking" -- Example endpoint

local function fetchTrackingData()
    local success, result = pcall(function()
        return HttpService:GetAsync(ARServerUrl)
    end)
    if success then
        return HttpService:JSONDecode(result)
    else
        warn("Failed to fetch AR data: " .. result)
        return nil
    end
end

local trackedPart = Instance.new("Part")
trackedPart.Name = "ARObject"
trackedPart.Parent = workspace

RunService.RenderStepped:Connect(function()
    local data = fetchTrackingData()
    if data then
        trackedPart.CFrame = CFrame.new(data.position.x, data.position.y, data.position.z) *
            CFrame.fromEulerAnglesXYZ(math.rad(data.rotation.x), math.rad(data.rotation.y), math.rad(data.rotation.z))
    end
end)
