using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AddFeatures
{
    public partial class Feature
    {
        [JsonProperty("attributes", NullValueHandling = NullValueHandling.Ignore)]
        public Dictionary<string, object> Attributes { get; set; }

        [JsonProperty("geometry", NullValueHandling = NullValueHandling.Ignore)]
        public IGeometry Geometry { get; set; }

        public object GetAttribute(string name)
        {
            string key = Attributes.Keys.FirstOrDefault(item => item.ToLower() == name.ToLower());
            if (!string.IsNullOrWhiteSpace(key))
            {
                return Attributes[key];
            }

            return null;
        }

        public T GetAttribute<T>(string name)
        {
            string key = Attributes.Keys.FirstOrDefault(item => item.ToLower() == name.ToLower());
            if (!string.IsNullOrWhiteSpace(key) && Attributes[key] is T attribute)
            {
                return attribute;
            }
            return default;
        }

        public bool AddOrUpdateAttribute(string name, object value)
        {
            if (Attributes.ContainsKey(name))
            {
                return UpdateAttribute(name, value);
            }
            else
            {
                Attributes.Add(name, value);
                return true;
            }
        }

        public bool UpdateAttribute(string name, object value)
        {
            string attribute = Attributes.Keys.FirstOrDefault(item => item.ToLower() == name.ToLower());
            if (attribute == null)
            {
                throw new ArgumentException($"attribute {name} not found");
            }

            if (Attributes.Remove(attribute))
            {
                Attributes.Add(attribute, value);
                return true;
            }

            return false;
        }
    }
}
